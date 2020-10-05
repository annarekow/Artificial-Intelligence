
"""
def plot(inputFile, inputX, inputLabel):
    # Initialize figure and plot initial data
    fig1 = plt.figure(1)
    # For plotting scaled data
    ax1 = fig1.add_subplot(121, projection='3d')
    plotX1scaled = np.arange(inputX[:, 1].min(), inputX[:, 1].max(), 0.2)
    plotX2scaled = np.arange(inputX[:, 2].min(), inputX[:, 2].max(), 0.2)
    plotX1scaled, plotX2scaled = np.meshgrid(plotX1scaled, plotX2scaled)
    ax1.set_xlabel('age(years)')
    ax1.set_ylabel('weight(kilograms)')
    ax1.set_zlabel('height(meters)')
    ax1.scatter(inputX[:, 1], inputX[:, 2], inputLabel)
    ax1.set_title('Scaled inputs')
    # For plotting unscaled data
    ax2 = fig1.add_subplot(122, projection='3d')
    plotX1unscaled = np.arange(inputFile[:, 0].min(), inputFile[:, 0].max(), 0.2)
    plotX2unscaled = np.arange(inputFile[:, 1].min(), inputFile[:, 1].max(), 0.2)
    plotX1unscaled, plotX2unscaled = np.meshgrid(plotX1unscaled, plotX2unscaled)
    ax2.set_xlabel('age(years)')
    ax2.set_ylabel('weight(kilograms)')
    ax2.set_zlabel('height(meters)')
    ax2.scatter(inputFile[:, 0], inputFile[:, 1], inputLabel)
    ax2.set_title('Unscaled inputs')
    # For plotting learning curve
    fig2 = plt.figure(2)
    ax3 = fig2.add_subplot(111)
    ax3.set_title('Learning Curve')



    plt.show()  ###
"""
    """
    # Initialize figure and plot initial data
    fig1 = plt.figure(1)
    # For plotting scaled data
    ax1 = fig1.add_subplot(121, projection='3d')
    plotX1scaled = np.arange(inputTrain[:, 1].min(), inputTrain[:, 1].max(), 0.2)
    plotX2scaled = np.arange(inputTrain[:, 2].min(), inputTrain[:, 2].max(), 0.2)
    plotX1scaled, plotX2scaled = np.meshgrid(plotX1scaled, plotX2scaled)
    ax1.set_xlabel('age(years)')
    ax1.set_ylabel('weight(kilograms)')
    ax1.set_zlabel('height(meters)')
    ax1.scatter(inputTrain[:, 1], inputTrain[:, 2], labels)
    ax1.set_title('Scaled inputs')
    # For plotting unscaled data
    ax2 = fig1.add_subplot(122, projection='3d')
    plotX1unscaled = np.arange(inputFile[:, 0].min(), inputFile[:, 0].max(), 0.2)
    plotX2unscaled = np.arange(inputFile[:, 1].min(), inputFile[:, 1].max(), 0.2)
    plotX1unscaled, plotX2unscaled = np.meshgrid(plotX1unscaled, plotX2unscaled)
    ax2.set_xlabel('age(years)')
    ax2.set_ylabel('weight(kilograms)')
    ax2.set_zlabel('height(meters)')
    ax2.scatter(inputFile[:, 0], inputFile[:, 1], labels)
    ax2.set_title('Unscaled inputs')
    # For plotting learning curve
    fig2 = plt.figure(2)
    ax3 = fig2.add_subplot(111)
    ax3.set_title('Learning Curve')
"""

""""""
        # Plot learning curve for current alpha value
        ax3.plot(range(len(risks)), risks)
        # PLot boundary surface for scaled data
        plotZ = (weights[0] + weights[1] * plotX1scaled + weights[2] * plotX2scaled)
        ax1.plot_surface(plotX1scaled, plotX2scaled, plotZ)
        # Plot boundary surface for unscaled data
        #weightUnscaled = unscaledWeight(weights, mean, std)
        #plotZunscaled = (weightUnscaled[0] + weightUnscaled[1] * plotX1unscaled + weightUnscaled[2] * plotX2unscaled)
        #ax2.plot_surface(plotX1unscaled, plotX2unscaled, plotZunscaled)
"""