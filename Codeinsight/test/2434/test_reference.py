import numpy as np

def test(arr0, arr1):
    return np.vstack((arr0, arr1)).reshape((-1,), order='F')
