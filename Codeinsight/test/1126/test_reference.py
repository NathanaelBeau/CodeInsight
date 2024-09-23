import numpy as np

def test(arr0, arr1):
    return np.ravel((arr0, arr1), order='F')

