import numpy as np
import sys
import math

def main():
    print("Welcome to Tyler See's Feature Selection Algorithm!")

    print("Type the number for a dataset.")
    print("1. Personal dataset")
    print("2. Custom dataset")
    personal = input()
    print()

    data, instances, features = readFile(personal)

    print("Type the number of the algorithm you want to run.")
    print("1. Forward Selection")
    print("2. Backward Elimination")
    alg = input()
    print()

    accuracy = leaveOneOut(data, [], -1)

    print()
    print("This dataset has", features - 1, "features (not including the class attribute), with", instances, "instances.")
    print()
    print("Running nearest neighbor with no features (default rate), using \"leaving-one-out\" evaluation, I get an accuracy of", str(accuracy) + "%")
    print()
    print("Beginning search.")
    print()

    if alg == "1":
        forward(data)
    else:
        backward(data)

def readFile(personal):
    if personal == "1":
        print("Choose a dataset:")
        print("1. CS170_Spring_2022_Small_data__62")
        print("2. CS170_Spring_2022_Large_data__62")
        choice = input()
        print()

        if choice == "1":
            name = "CS170_Spring_2022_Small_data__62.txt"
        else:
            name = "CS170_Spring_2022_Large_data__62.txt"
    else:
        name = input("Input file name: ")

    data = np.loadtxt(name)
    return data, np.shape(data)[0], np.shape(data)[1]

def leaveOneOut(data, currSet, addFeat):
    if addFeat != -1:
        currSet = currSet.copy()
        currSet.append(addFeat)

    numCorrect = 0

    for i in range(len(data)):
        classify = []
        for feature in currSet:
            classify.append(data[i][feature])

        currClass = data[i][0]
        nnDistance = sys.maxsize
        nnLocation = sys.maxsize

        for j in range(len(data)):
            if j != i:
                check = []
                for feature in currSet:
                    check.append(data[j][feature])

                distance = math.dist(classify, check)
                if distance < nnDistance:
                    nnDistance = distance
                    nnLocation = j
                    nnClass = data[nnLocation][0]

        # print(i + 1, "is in class", currClass)
        # print("Nearest neighbor is", str(nnLocation + 1) + ", in class", nnClass)

        if currClass == nnClass:
            numCorrect += 1

    accuracy = numCorrect / len(data)
    return accuracy
        

def forward(data):
    currFeat = []
    solution = []
    bestAcc = 0
    
    for i in range(1, len(data[0])):
        addFeat = 0
        currBestAcc = 0
        for j in range(1, len(data[0])):
            if j not in currFeat:
                accuracy = leaveOneOut(data, currFeat, j)
                print("Using feature(s)", str(currFeat + [j]), "accuracy is", str(accuracy) + "%")
                if accuracy > currBestAcc:
                    currBestAcc = accuracy
                    addFeat = j
        
        if currBestAcc < bestAcc:
            print("Warning, Accuracy has decreased!")
            print()
            break
        bestAcc = currBestAcc
        solution.append(addFeat)
        currFeat.append(addFeat)
        print("Feature set", str(currFeat), "was best, accuracy is", str(currBestAcc) + "%")
        print()

    print("Finished search! The best feature subset is", str(solution), "which has an accuracy of", str(bestAcc) + "%")

    
def backward(data):
    currFeat = []
    solution = []
    bestAcc = 0

    for i in range(1, len(data[0])):
        currFeat.append(i)

    for i in range(1, len(data[0]) - 1):
        remFeat = 0
        currBestAcc = 0
        for j in currFeat:
            removed = currFeat.copy()
            removed.remove(j)
            accuracy = leaveOneOut(data, removed, -1)

            print("Removing", str(j), "using feature(s)", str(currFeat), "accuracy is", str(accuracy) + "%")
            if accuracy > currBestAcc:
                currBestAcc = accuracy
                solution = currFeat.copy()
                remFeat = j

        if currBestAcc < bestAcc:
            print("Warning, Accuracy has decreased!")
            print()
            break
        bestAcc = currBestAcc
        solution = currFeat.copy()
        currFeat.remove(remFeat)
        print("Feature set", str(currFeat), "was best, accuracy is", str(currBestAcc) + "%")
        print()

    print("Finished search! The best feature subset is", str(solution), "which has an accuracy of", str(bestAcc) + "%")

main()
