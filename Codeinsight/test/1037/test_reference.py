from sklearn.cluster import KMeans
import numpy as np

def test(arr0):
    x = np.array(arr0)
    n_clusters = 5  # Adjust the number of clusters as desired
    km = KMeans(n_clusters=n_clusters)
    km.fit(x.reshape(-1, 1))
    labels = km.labels_
    return labels


