''' (cdz) cmsc723 final 2024 '''

# let's see how llm's handle basic math! 

# possible improvements: 
#   - returning model output rather than just invalid/valid-correct/valid-incorrect
#     to see just how wrong the models are
#   - improve checking answer function (speed / logic is eh)
#   - code linting because this is bad lol 

import argparse
import transformers
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import re
import random
import json
from tqdm import tqdm
from torch.cuda.amp import autocast
from huggingface_hub import login

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

q4 = "Q: Jason had 20 lollipops. He gave Denny some lollipops. Now Jason has 12 lollipops. "\
    "How many lollipops did Jason give to Denny?\n" + \
    "A: Let's think step by step. Jason started with 20 lollipops. Then he had 12 after giving some to Denny. "\
    "So he gave Denny 20 - 12 = 8. The answer is 8."

q5 = "Q: Shawn has five toys. For Christmas, he got two toys each from his mom and dad. "\
    "How many toys does he have now?\n" + \
    "A: Let's think step by step. Shawn started with 5 toys. If he got 2 toys each from his mom and dad, "\
    "then that is 4 more toys. 5 + 4 = 9. The answer is 9."

q6 = "Q: There were nine computers in the server room. Five more computers were installed each day, "\
    "from Monday to Thursday. How many computers are now in the server room?\n" + \
    "A: Let's think step by step. There were originally 9 computers. For each of 4 days, 5 more computers were added. "\
    "So 5 * 4 = 20 computers were added. 9 + 20 is 29. The answer is 29."

q7 = "Q: Michael had 58 golf balls. On Tuesday, he lost 23 golf balls. On Wednesday, " \
    "he lost 2 more. How many golf balls did he have at the end of Wednesday?\n" + \
    "A: Let's think step by step. Michael started with 58 golf balls. After losing 23 on Tuesday, he had 58 - 23 = 35. "\
    "After losing 2 more, he had 35 - 2 = 33 golf balls. The answer is 33."

q8 = "Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?\n" + \
    "A: Let's think step by step. Olivia had 23 dollars. 5 bagels for 3 dollars each will be 5 x 3 = 15 dollars. "\
    "So she has 23 - 15 dollars left. 23 - 15 is 8. The answer is 8."
### / CoT Prompt String. 

COT_PROMPT = preamble+'\n'+q1+'\n'+q2+'\n'+q3+'\n'+q4+'\n'+q5+'\n'+q6+'\n'+q7+'\n'+q8+'\n'
LTSBS = "Let's think step by step. "

ANSWER_PHRASE = "The answer is"
INVALD_RESPONSE = "<inv>"
VALID_CORRECT = "<vc>"
VALID_INCORRECT = "<vi>"
NUM_RE = re.compile(r"-?\d+[\d,]*\.?\d*")
TEST_RE = re.compile(r"#### (\-?[0-9\.\,]+)")
HF_TOKEN = "" # replace with your hf login token :)
MAX_TOKENS = 1024
DEVICE = 'cuda'
DEBUGGING = False
SEED = 23 # pick any here idk 
SAMPLES = 20
GSM8K_DATA = './data/gsm8k_test.jsonl'

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model",
        type=str,
        default="google/gemma-7b-it",
        help="hf model-name",
    )
    # TODO (cdz) : this isn't used; maybe just use the json path?
    #              or not, with symbolic templates in mind
    parser.add_argument(
        "--in",
        type=str,
        default="./data",
        help="directory with data",
    )

    parser.add_argument(
        "--out",
        type=str,
        default="./output",
        help="output directory",
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="enable debugging"
    )

    parser.add_argument(
        "--dq",
        action="store_true",
        help="don't quantize model"
    )


    argvs = parser.parse_args()
    return argvs

def load_model(hf_name,hf_token=HF_TOKEN,dq=False):
    '''
    Load the desired hf model/tokenizer and return 
    '''
    login(hf_token)
    print('-'*25+'Loading Model: ' + hf_name + ' '+ '-'*25)
    tokenizer = AutoTokenizer.from_pretrained(hf_name)
    model = AutoModelForCausalLM.from_pretrained(hf_name)
    if not dq:
        model.half()
    print("Loading device to cuda.... ")
    model.to(DEVICE)
    print("Done loading to cuda!")
    # not sure if we need eval here
    model.eval()
    print('-'*25 + "Finished loading"+ '-'*25)
    return model, tokenizer

def extract_and_clean_numbers(response):
    '''
    given string, return the numbers contained in it, with commas cleaned. 
    '''
    numbers = NUM_RE.findall(response)
    nums = [] # store numbers without commas. 
    for num in numbers:
        # remove commas. 
        clean = num.replace(",", "")
        clean = clean.strip()
        nums.append(clean)
    return nums

def extract_clean_number(num:str):
    """
    if we have a cleaned string that is just a number. 
    """
    num = num.replace(",","")
    num = num.strip()
    return num

def check_response(response:str,answer:str):
    '''
    Check the response of a model (str) for correctness 
    Args:
    reponse -- the model's output/response
    answer -- the correct answer. assuming this is a str
    '''
    response = response.lower()
    answer = extract_clean_number(answer.strip())

    # handle if our answer phrase is in the response
    if ANSWER_PHRASE in response:
        chunks = response.split(ANSWER_PHRASE.lower())
        if len(chunks) == 2:
            nums = extract_and_clean_numbers(chunks[-1])
            if not nums: 
                return INVALD_RESPONSE
            if answer in nums:
                return VALID_CORRECT
            return VALID_INCORRECT
        # bad logic here, but should work. 
        else:
            for i in range(len(chunks)):
                if i%2 == 0:
                    nums = extract_and_clean_numbers(chunks[i])
                    if answer in nums:
                        return VALID_CORRECT
            return INVALD_RESPONSE
    # otherwise, just check for correct number. 
    else:
        nums = extract_and_clean_numbers(response)
        if not nums: 
            return INVALD_RESPONSE
        else: 
            for num in nums:
                num = num.strip() # just in case 
                if num == answer:
                    return VALID_CORRECT
            return VALID_INCORRECT
    
    # TODO : Finish this function. 
    pass

def create_prompt(question):
    '''
    generate the prompt for a given question 
    (here, question is from the gsm8k json, maybe? really just a string 
    that has as question with no whitespace)
    '''
    # just in case, TODO remove (cdz)
    question = question.strip()

    prompt = COT_PROMPT + 'Q: ' + question + "\n" + "A: " + LTSBS
    return prompt

def infer(model, tokenizer, prompt): 
    '''
    generate the response. 
    '''
    torch.cuda.empty_cache() # just in case 
    model_inputs = tokenizer([prompt], return_tensors="pt").to(DEVICE)

    with torch.no_grad():
        # infer
        generated_ids = model.generate(**model_inputs, max_new_tokens=MAX_TOKENS,
                                        do_sample=False, num_return_sequences=1)
        
        # Decode and return
        result = tokenizer.batch_decode(generated_ids)[0]
        return result

def pick_samples(questions, s=True):
    '''
    pick #SAMPLES from all gsm8k questions.  
    args:
    bool s : whether to seed or not
    '''
    if s: # should probably be false for actual data collection. 
        random.seed(SEED)
    # question answer pairs
    qaps = random.sample(questions, SAMPLES)
    return qaps

def main():
    argvs = parse_args()
    model,tokenizer = load_model(argvs.model,dq=argvs.dq)
    qa_combos = []

    # jsonl file; bit different than json
    with open(GSM8K_DATA, 'r') as file:
        for line in file:
            d = json.loads(line)
            q = d['question']
            n = TEST_RE.search(d['answer'])
            a = n.group(1).strip()
            a = a.replace(",", "")
            qa_combos.append((q,a))
    print(qa_combos)

    tests = pick_samples(qa_combos)

    counts = {VALID_CORRECT: 0, VALID_INCORRECT:0, INVALD_RESPONSE:0}

    for test in tqdm(tests):
        question = test[0]
        answer = test[1]
        prompt = create_prompt(question)
        response = infer(model,tokenizer,prompt)
        if DEBUGGING:
            print('-'*25 + 'DEBUG MODEL RESPONSE' + '-'*25)
            print('Question :' + question)
            print('Model Response: ' + response)
            print('Answer: ' + answer)
            print(' CORRECT? : ' + check_response(response,answer))
            print('-'*23 + 'end DEBUG MODEL RESPONSE' + '-'*23)
        ans = check_response(response,answer)
        counts[ans] += 1
    
    outpath = argvs.out + '/' + argvs.model + '-' + 'results'
    # TODO: Save test outputs. 
    with open(outpath, 'w') as f:
        for key, value in counts.items():
            f.write(f"{key}: {value}\n")

    print('done!')

if __name__ == "__main__":
    ### cli functionality here. 
    main()