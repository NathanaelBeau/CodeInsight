import numpy as np

def test(arr0, var0):
    indices = np.where(arr0 == var0)
    return indices