import numpy as np

def test(arr0, arr1):
    return np.hstack(list(zip(arr0, arr1)))

