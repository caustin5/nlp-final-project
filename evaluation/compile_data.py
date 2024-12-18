import os
import argparse
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

INVALID_RESPONSE = "<inv>:"
VALID_CORRECT = "<vc>:"
VALID_INCORRECT = "<vi>:"

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory",
        type=str,
        default="",
        help="directory location for data",
    )

    args = parser.parse_args()
    return args

def main():


    args = parse_args()
    dir_in_str = args.directory

    results = []
    sum_accuracies = []
    hues = []

    fig, axes = plt.subplots(3,4)
    axes[0,0].set_title("gemma-2-2b")
    axes[0,1].set_title("llama-3.2-1b")
    axes[0,2].set_title("phi-3.5-mini")
    axes[0,3].set_title("rho-math-1b")

    axes[0,0].set_ylabel("clause")
    axes[1,0].set_ylabel("gsm")
    axes[2,0].set_ylabel("sym")
    axes[0,1].set_ylabel(" ")
    axes[1,1].set_ylabel(" ")
    axes[2,1].set_ylabel(" ")
    axes[0,2].set_ylabel(" ")
    axes[1,2].set_ylabel(" ")
    axes[2,2].set_ylabel(" ")
    axes[0,3].set_ylabel(" ")
    axes[1,3].set_ylabel(" ")
    axes[2,3].set_ylabel(" ")


    datas = ["clause", "gsm", "sym"]
    models = ["gemma-2-2b", "llama-3.2-1b", "phi-3.5-mini","rho-math-1b"]

    tuples = []
    titles = []

    for i in range(3):
        for j in range(4):
            tuples.append((i,j))
            titles.append(models[j])


    i = 0
    j = 0


    for sub_dir_data in os.listdir(dir_in_str):
        total = 0
        total_correct = 0
        total_incorrect = 0

        result = {}
        accuracies = []

        for sub_dir_model in os.listdir(dir_in_str + "\\" + sub_dir_data):
            for filename in os.listdir(dir_in_str + "\\" + sub_dir_data + "\\" + sub_dir_model):
                if filename.endswith(".txt"): 
                    with open(dir_in_str + "\\" + sub_dir_data + "\\" + sub_dir_model + "\\" + filename) as f:
                        lines = f.readlines()
                        current_total = 0
                        current_correct = 0
                        current_incorrect = 0
                        for line in lines:
                            if line.startswith(INVALID_RESPONSE):
                                l = line.replace(INVALID_RESPONSE,"")
                                l = l.strip()
                                current_total += int(l)
                                total += int(l)

                            if line.startswith(VALID_CORRECT):
                                l = line.replace(VALID_CORRECT,"")
                                l = l.strip()
                                current_total += int(l)
                                current_correct += int(l)
                                total += int(l)
                                total_correct += int(l)

                            if line.startswith(VALID_INCORRECT):
                                l = line.replace(VALID_INCORRECT,"")
                                l = l.strip()
                                current_total += int(l)
                                current_incorrect += int(l)
                                total += int(l)
                                total_incorrect += int(l)
                        accuracies.append(current_correct/current_total)
                else:
                    continue

            sns.histplot(accuracies,kde=True,ax=axes[tuples[i][0],tuples[i][1]], bins=8, binrange=[0,.8])


            result["title"] = sub_dir_data + ": " + sub_dir_model
            result["total"] = total
            result["total_correct"] = total_correct
            result["total_incorrect"] = total_incorrect
            if total > 0:
                result["accuracy"] = total_correct/total
            else:
                result["accuracy"] = 0
            


            sum_accuracies.append(result["accuracy"])
            hues.append(datas[j])
            
            i+=1

            results.append(result) 

        j += 1

    
    

    plt.show()

    d = {"title": titles, "accuracy": sum_accuracies, "hues": hues}
    data1 = pd.DataFrame(data = d)

    print(data1)

    hue_map = {datas[0]:"red", datas[1]:"yellow", datas[2]:"black"}

    plt.figure()
    sns.barplot(data1,x="accuracy", y="title",hue=hues, palette=hue_map, legend=True)
    plt.ylabel("Language Model")
    plt.show()

    diffs = []
    for i in range(4):
        print(data1.loc[4+i,"accuracy"])
        diffs.append(data1.loc[8+i,"accuracy"] - data1.loc[4+i,"accuracy"])

    print(diffs)

    e = {"title": models, "diff": diffs}
    data2 = pd.DataFrame(data = e)


    plt.figure()
    sns.barplot(data2,x="title", y="diff")
    plt.xlabel("Language Model")
    plt.ylabel("%")
    plt.title("Drop in Accuracy from GSM to GSM-Symbolic")
    plt.show()

    
main()



