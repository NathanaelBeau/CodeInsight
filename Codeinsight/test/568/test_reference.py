import numpy as np

def test(arr0, arr1):
    return np.any(np.in1d(arr0, arr1))