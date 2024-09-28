import numpy as np

def test(arr0, arr1):
    return np.sqrt(((arr0 - arr1) ** 2).sum(-1))
