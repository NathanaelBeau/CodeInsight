import numpy as np

def test(arr0, var0):
    indices = list(zip(*np.where(arr0 == var0)))
    return indices

