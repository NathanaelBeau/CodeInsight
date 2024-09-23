import numpy as np

def test(arr0, var0):
    indices = np.argwhere(arr0 == var0)
    return indices

