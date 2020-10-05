# Things to think about:
# risk should go down each time, otherwise alpha value is too big
# scale the features to ensure that you're not giving advantage to a specific direction or feature
# if your epsilon is less than 0.01 then declare convergence!
# input format: python lr.py data2.csv results2.csv
# data2 formatting: [age, weight, height] - predicting height using age and weight

# Linear regression formula f(x) = B0 + B1 + B2 (for two features)

import sys
import numpy as np
import csv


def linReg(inputTrain, labels, outputName):
    # Open csv file for writing
    file = open(outputName, 'w', newline='')
    out = csv.writer(file)

    # Initialize the learning rates
    alphas = [0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1, 5, 10, 1]
    iterations = [100, 100, 100, 100, 100, 100, 100, 100, 100, 77]
    n = len(inputTrain)

    # values for learning rate and iteration analysis
    # bestAlpha = 0.0
    # bestI = 0.0
    # bestRisk = 10000000000.0

    for alpha, iterate in zip(alphas, iterations):
        risks = []
        weights = np.zeros(inputTrain.shape[1])
        for i in range(iterate):
            f = inputTrain.dot(weights)  # f = b0 + b1x1 + ...
            risk = (1 / (2 * n)) * sum((f - labels.flatten()) ** 2)  # risk function
            risks.append(risk)  # add to list

            # Gradient descent calculation
            diff = (f[:, None] - labels).flatten()
            weights = weights - (alpha / n) * ((inputTrain * diff[:, None]).sum(axis=0))

            """
            # To find the best rate and iteration values
            if risk < bestRisk:
                if i == 0:
                    bestRisk = risk
                    bestAlpha = alpha
                    bestI = i
                elif i > 0 and risk < risks[i - 1]:  # if risk is moving in descending order
                    bestRisk = risk
                    bestAlpha = alpha
                    bestI = i
                elif risk > risks[i - 1]:  # need different alpha value
                    break

            print("alpha: ", bestAlpha, ", iteration: ", bestI, ", minRisk: ", bestRisk)
            """

        # Write weight vector to csv file for current alpha value
        val = np.hstack((alpha, iterate, weights))
        out.writerow(val)

    # Close csv file
    file.close()


def main():
    inputData = np.genfromtxt(sys.argv[1], delimiter=',')  # data2.csv
    outputName = sys.argv[2]  # results2.csv

    # Normalize data
    mean = inputData[:, :-1].mean(axis=0)
    std = inputData[:, :-1].std(axis=0)
    normalizedData = (inputData[:, :-1] - mean[None, :]) / std[None, :]  # from hw - Xscaled equation

    inputTrain = np.c_[np.ones(len(inputData)), normalizedData]  # add 1's in the front for linreg bias function
    labels = inputData[:, -1:]

    # Call linear regression learning algorithm
    linReg(inputTrain, labels, outputName)


if __name__ == "__main__":
    main()