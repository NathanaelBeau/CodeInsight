import numpy as np

def test(arr0):
    return np.sum(np.arange(len(arr0)) * arr0) / np.sum(arr0)
