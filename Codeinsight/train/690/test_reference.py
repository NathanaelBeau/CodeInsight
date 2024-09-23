import numpy as np

def test(arr0):
    arr = np.vstack((arr0 - 1, arr0, arr0 + 1))
    arr[:, ::2] = 0
    return arr