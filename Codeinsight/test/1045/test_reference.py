import numpy as np

def test(arr0, arr1):
    return np.ravel(np.column_stack((arr0, arr1)))

