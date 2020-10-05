import numpy as np
import cv2
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

treesImage = cv2.imread('./trees.png')
treesImage = cv2.cvtColor(treesImage, cv2.COLOR_BGR2RGB)

# Reshape the image to work with the 3D space of RGB
img = treesImage.reshape((-1, 3))
img = np.float32(img)

# K Means with diff K values
for K in range(2, 7):
    kmeans = KMeans(n_clusters=K).fit(img)
    centers = kmeans.cluster_centers_
    labels = kmeans.labels_

    # Reshape
    center = np.uint8(centers)
    res = center[labels.flatten()]
    result_image = res.reshape((treesImage.shape))

    """
    # Visualize
    figure_size = 8
    plt.figure(figsize=(figure_size,figure_size))
    plt.subplot(1,2,1),plt.imshow(treesImage)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(1,2,2),plt.imshow(result_image)
    plt.title('K Means K = %i' % K), plt.xticks([]), plt.yticks([])
    plt.show()
    """
