import numpy as np

def test(arr0: np.ndarray, arr1: np.ndarray) :
    return np.mean(np.array([arr0, arr1]), axis=0)

