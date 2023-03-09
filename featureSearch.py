import numpy as np
import time
import random

def main():
    # print("Welcome to Tyler See's Feature Selection Algorithm!")

    # num = input("Please enter total number of features: ")
    # print()

    # print("Type the number of the algorithm you want to run.")
    # print("-Forward Selection")
    # print("-Backward Elimination")
    # alg = input()

    data = readFile()
    forward()

def readFile():
    name = input("Input file name: ")

    data = np.loadtxt(name)
    return data   

def forward():
    currFeat = []
    solution = []
    bestAcc = 0
    

    for i in range(1, 5):
        addFeat = 0
        currBestAcc = 0
        for j in range(1, 5):
            if j not in currFeat:
                accuracy = random.randint(0, 1000) / 10
                print("Using feature(s)", str(currFeat + [j]), "accuracy is", str(accuracy) + "%")
                if accuracy > currBestAcc:
                    currBestAcc = accuracy
                    addFeat = j
        
        if currBestAcc < bestAcc:
            print("Warning, Accuracy has decreased!")
            break
        bestAcc = currBestAcc
        solution.append(addFeat)
        currFeat.append(addFeat)
        print("Feature set", str(currFeat), "was best, accuracy is", str(currBestAcc) + "%")
        print()

    print("Finished search! The best feature subset is", str(solution), "which has an accuracy of", str(bestAcc) + "%")

    

def backward():
    pass

main()
