import numpy as np

def test(arr0):
    unique, counts = np.unique(arr0, return_counts=True)
    return dict(zip(unique, counts))

