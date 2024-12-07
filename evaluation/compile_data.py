import os
import argparse
import seaborn as sns
import matplotlib.pyplot as plt

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
    sum_accuracies = {}

    fig, axes = plt.subplots(1,2)
    i = 0


    for sub_dir_in_str in os.listdir(dir_in_str):
        total = 0
        total_correct = 0
        total_incorrect = 0

        result = {}
        accuracies = []


        for filename in os.listdir(dir_in_str + "\\" + sub_dir_in_str):
            if filename.endswith(".txt"): 
                with open(dir_in_str + "\\" + sub_dir_in_str + "\\" + filename) as f:
                    lines = f.readlines()
                    for line in lines:
                        if line.startswith(INVALID_RESPONSE):
                            l = line.replace(INVALID_RESPONSE,"")
                            l = l.strip()
                            total += int(l)

                        if line.startswith(VALID_CORRECT):
                            l = line.replace(VALID_CORRECT,"")
                            l = l.strip()
                            total += int(l)
                            total_correct += int(l)
                            accuracies.append(int(l))

                        if line.startswith(VALID_INCORRECT):
                            l = line.replace(VALID_INCORRECT,"")
                            l = l.strip()
                            total += int(l)
                            total_incorrect += int(l)
            else:
                continue
        sns.histplot(accuracies,kde=True,ax=axes[i])
        i+=1


        result["title"] = sub_dir_in_str
        result["total"] = total
        result["total_correct"] = total_correct
        result["total_incorrect"] = total_incorrect
        if total > 0:
            result["accuracy"] = total_correct/total
        else:
            result["accuracy"] = 0

        sum_accuracies[sub_dir_in_str] = result["accuracy"]

        results.append(result) 
    
    plt.show()

    plt.figure()
    sns.barplot(sum_accuracies)
    plt.show()

    
main()



