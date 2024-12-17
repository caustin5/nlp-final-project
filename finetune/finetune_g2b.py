""" (cdz) fine-tuning a model on gsm-symbolic (our version) """

from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, TrainingArguments
from transformers import pipeline, logging
import torch
from tqdm import tqdm
from huggingface_hub import login
from transformers.models.gemma2.modeling_gemma2 import Gemma2ForCausalLM
from datasets import Dataset
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling
import os
import argparse
import transformers
import re
import random
import json
import time
import typing
from functools import partial

### CoT Prompt String.
preamble = "As an expert problem solver, solve step by step the following mathematical questions."
q1 = "Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. "\
    "After they are done, there will be 21 trees. How many trees did the grove workers plant today?\n" + \
    "A: Let's think step by step. There are 15 trees originally. Then there were 21 trees after some more were planted. "\
    "So there must have been 21 - 15 = 6. The answer is 6."

q2 = "Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are "\
    "in the parking lot?\n" + \
    "A: Let's think step by step. There are originally 3 cars. 2 more cars arrive. 3 + 2 = 5. The answer is 5."

q3 = "Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do "\
    "they have left in total?\n" + \
    "A: Let's think step by step. Originally, Leah had 32 chocolates. Her sister had 42. So in total they had " \
    "32 + 42 = 74. After eating 35, they had 74 - 35 = 39. The answer is 39."

### / CoT Prompt String. 

COT_PROMPT = preamble+'\n'+q1+'\n'+q2+'\n'+q3+'\n'
LTSBS = "Let's think step by step. "

DEVICE = "cuda"
HF_TOKEN = "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" # replace with your hf login token :)
MODEL = 'google/gemma-2-2b-it'
MODEL_FT = 'gemma-2-2b-it-gsmsymbolic'


def load_model(hf_name,hf_token=HF_TOKEN):
    '''
    load the desired hf model/tokenizer and return 
    '''
    login(hf_token)
    attn = "flash_attention_2"
    print('-'*25+'Loading Model: ' + hf_name + ' '+ '-'*25)

    tokenizer = AutoTokenizer.from_pretrained(hf_name)
    model = AutoModelForCausalLM.from_pretrained(hf_name,torch_dtype=torch.float16)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    print("Loading device to cuda.... ")
    model.to(DEVICE)
    print("Done loading to cuda!")
    # not sure if we need eval here
    model.eval()
    print('-'*25 + "Finished loading"+ '-'*25)
    return model, tokenizer

def create_prompt(question):
    '''
    given a question, insert it into the n-shot prompt. 
    '''
    # just in case, TODO remove (cdz)
    for q in question : q.strip()
    prompt = []
    for q in question : prompt.append(COT_PROMPT + 'Q: ' + q + "\n" + "A: " + LTSBS)
    return prompt

def format_training(example):
    # Tokenizing the 'question' as the prompt and 'answer' as the expected output
    print(example)
    hf_name = 'google/gemma-2-2b-it'
    tokenizer = AutoTokenizer.from_pretrained(hf_name)
    input_text = example['question']
    target_text = example['answer']
    
    # Tokenize input text (question)
    model_inputs = tokenizer(input_text, truncation=True, padding='max_length', max_length=512, return_tensors='pt')
    
    # Tokenize target text (answer), same max_length for consistency
    labels = tokenizer(target_text, truncation=True, padding='max_length', max_length=512, return_tensors='pt')
    
    # Extract input_ids for both input and labels
    model_inputs["labels"] = labels["input_ids"]
    
    # Flatten the tensors if necessary (convert from PyTorch tensors to lists of ints)
    model_inputs["input_ids"] = model_inputs["input_ids"].squeeze().tolist()  # Make sure input_ids is a flat list
    model_inputs["labels"] = model_inputs["labels"].squeeze().tolist()  # Make sure labels is a flat list

    return model_inputs

'''
Implementing from scratch: put on hold for now. 
'''

def find_linear_layers(model):
    lin = torch.nn.Linear
    lin_mod_names = set()
    for name, module in model.named_modules():
        if isinstance(module,lin):
            names = name.split('.')
            lin_mod_names.add(names[-1])
    if 'lm_head' in lin_mod_names:
        lin_mod_names.remove('lm_head')
    return list(lin_mod_names)
    

class LoRALayer(torch.nn.Module):
    def __init__(self, in_dim: int, out_dim: int, rank: int, alpha: float):
        """
        Initialize a LoRA with two weight matrices whose product is the same as the original parameter matrix.
        """
        super().__init__()

        self.dtype = torch.float16

        std = 1 / torch.sqrt(torch.tensor(rank).float())
        self.A = torch.nn.Parameter(torch.randn(in_dim, rank, dtype=self.dtype) * std)
        self.B = torch.nn.Parameter(torch.zeros(rank,out_dim, dtype=self.dtype))
        self.alpha = alpha
        
        torch.nn.init.kaiming_uniform_(self.A, a=5**1/2)
        torch.nn.init.zeros_(self.B)

        # Complete the initialization of the two weight matrices
        self.alpha = alpha

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Compute the linear layer's original result, then add the low-rank delta
        """
    
        return self.alpha * (x @ self.A @ self.B)


class LinearLoRA(torch.nn.Module):
    def __init__(self, linear: torch.nn.Linear, rank: int, alpha: float):
        """
        Initialize a Linear layer with LoRA adaptation.
        """
        super().__init__()
        self.linear = linear

        # Initialize the LoRA layer
    
        self.lora = LoRALayer (linear.weight.shape[1], linear.out_features, rank, alpha)
        

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass with LoRA adatpation.
        """
        result = self.linear(x) + self.lora(x)

        # Add the LoRA delta
        return result

def add_lora(model: torch.nn.Module, rank: int, alpha: float, 
             modules_to_adapt = {"attention": ["q_lin", "k_lin", "v_lin", "out_lin"], "ffn": ["lin1", "lin2"]}):
    """
    Add LoRA layers to a PyTorch model.  S

    Args:
        model: The PyTorch model to adapt.
        rank: The rank of the LoRA matrices.
        alpha: The scaling factor for the LoRA matrices.
        modules_to_adapt: The key of the dictionary is the model component to adapt (e.g., "attention" or "ffn"), and the values are specific linear layers in that component to adapt.  Anything in this dictionary will be adapted, but anything else will remain frozen.
    """
    # print(model)

    partial_lora = partial(LinearLoRA, rank=rank, alpha=alpha)

    for layer in model.model.layers: 

        # print(layer)

        layer.self_attn.q_proj = partial_lora(layer.self_attn.q_proj)
        layer.self_attn.k_proj = partial_lora(layer.self_attn.k_proj)
        layer.self_attn.v_proj= partial_lora(layer.self_attn.v_proj)
        layer.self_attn.o_proj = partial_lora(layer.self_attn.o_proj)

        layer.mlp.gate_proj = partial_lora(layer.mlp.gate_proj)
        layer.mlp.up_proj = partial_lora(layer.mlp.up_proj)
        layer.mlp.down_proj = partial_lora(layer.mlp.down_proj)
        # print(model)
    return model

def main():
    # hardcoding model for now. 
    model,tokenizer = load_model('google/gemma-2-2b-it',HF_TOKEN)
    eos_token = tokenizer.eos_token

    # Freezing model parameters
    for param in model.parameters():
        param.requires_grad = False

    # Default hyperparameters (can be organized later)
    lora_r = 16
    lora_alpha = 32
    lora_dropout = 0.05

    add_lora(model, lora_r, lora_alpha)
    print("-"*25+'Checkpoint: Lora Layer Added!'+"-"*25)
    
    # TODO (cdz) : adapt the model for lora finetuning. 

    max_tokens = 1024

    import json
    raw_data = {'input_ids': [], 'labels': []}
    # dump both json into this
    with open('gsm_symbolic_1-25_n=15.json', 'r') as file:
        data = json.load(file)
    for entry in data:
        for key, value in entry.items():
            if key.startswith('question_'):
                question_num = key.split('_')[1]
                answer_key = f"answer_{question_num}"
                if answer_key in entry:
                    raw_data['input_ids'].append(value)
                    raw_data['labels'].append(entry[answer_key])                
    
    with open('gsm_symbolic_1-25_n=50.json', 'r') as file:
        data = json.load(file)
    for entry in data:
        for key, value in entry.items():
            if key.startswith('question_'):
                question_num = key.split('_')[1]
                answer_key = f"answer_{question_num}"
                if answer_key in entry:
                    raw_data['input_ids'].append(value)
                    raw_data['labels'].append(entry[answer_key])
    

    dataset = Dataset.from_dict(raw_data)
    tokenized_dataset = dataset.map(
        lambda examples: {
            'input_ids': tokenizer(examples['input_ids'], truncation=True, padding="max_length",
                                    max_length=max_tokens, return_tensors='pt').input_ids,
            'labels': tokenizer(examples['labels'], truncation=True, padding="max_length",
                                 max_length=max_tokens, return_tensors='pt').input_ids
            },
            batched=True
            )
    tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.2)

    reduction_factor = 0.20  # Keep 25% of the original training data
    train_subset_size = int(len(tokenized_dataset['train']) * reduction_factor)
    tokenized_dataset['train'] = tokenized_dataset['train'].select(range(train_subset_size))
    # setting up finetune

    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=2,
        per_device_train_batch_size=2,
        per_device_eval_batch_size=2,
        logging_dir='./logs',
        logging_steps=100,
        save_steps=500,
        evaluation_strategy="epoch",
        weight_decay=0.01
        )
    
    data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

    trainer = Trainer(
        model = model,
        args = training_args,
        train_dataset = tokenized_dataset['train'],
        eval_dataset = tokenized_dataset['test'],
        data_collator = data_collator
        )
    
    
    print('-'*25 + ' Fine-tuning! ' + '-'*25)
    trainer.train()
    print('-'*22 + ' Finished Fine-tuning ' + '-'*22)

    
    trainer.save_model('./results/fine_tuned_test1')
    print('-'*25 + ' HF Model Saved' + '-'*25)
    torch.save(model.state_dict(), './results/fine_tuned_test1/lora_finetuned_model.pt')
    print('-'*23 + ' LoRA Model Saved' + '-'*23)


if __name__ == "__main__":
    main()