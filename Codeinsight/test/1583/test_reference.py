import numpy as np
from sklearn.cluster import KMeans

def test(arr0, n_clusters):
    # Reshape arr0 into a 2D array for KMeans
    arr0_reshaped = arr0.reshape(-1, 1)

    # Perform KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=0)
    kmeans.fit(arr0_reshaped)

    # Return the cluster labels and cluster centers
    return kmeans.labels_