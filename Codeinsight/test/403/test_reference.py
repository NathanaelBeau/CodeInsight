import numpy as np

def test(arr0, arr1):
    return np.dstack((arr0, arr1)).flatten()

