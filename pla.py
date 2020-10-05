# python pla.py data1.csv results1.csv

import sys
import numpy as np
import csv
from matplotlib import pyplot as plt


def visualize(inputData, weights):
    positive = inputData[inputData[:, 2] == 1, :]
    negative = inputData[inputData[:, 2] == -1, :]

    plt.scatter(positive[:, 0], positive[:, 1], c='#ff7f0e', marker='o')
    plt.scatter(negative[:, 0], negative[:, 1], c='#17becf', marker='o')

    x = np.linspace(min(inputData[:, 0]), max(inputData[:, 0]))
    y = (-weights[0] * x - weights[2]) / weights[1]
    plt.plot(x, y, 'k')
    plt.show()


def perceptron(inputTrain, labels, outputName):
    weights = np.zeros(inputTrain.shape[1])  # initialize weights: [0, 0, 0]

    file = open(str(outputName), 'w', newline='')
    out = csv.writer(file)

    notConverged = 1
    while notConverged:
        notConverged = 0
        for point, label in zip(inputTrain, labels):
            f = point.dot(weights)
            if label * f <= 0:
                weights = weights + label * point
                notConverged = 1
        out.writerow(weights)

    file.close()
    return weights


def main():
    inputData = np.genfromtxt(sys.argv[1], delimiter=',')
    outputName = sys.argv[2]
    inputTrain = np.c_[inputData[:, :-1], np.ones(len(inputData))]  # add column at the end for bias
    labels = inputData[:, -1:]

    perceptron(inputTrain, labels, outputName)

    # for visualization
    # weights = perceptron(inputTrain, labels, outputName)
    # visualize(inputData, weights)  # visualization function


if __name__ == "__main__":
    main()
