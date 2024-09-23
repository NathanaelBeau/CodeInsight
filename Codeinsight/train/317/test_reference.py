import numpy as np
def test(arr0, arr1):
    return np.nonzero(np.in1d(arr1, arr0))[0]

