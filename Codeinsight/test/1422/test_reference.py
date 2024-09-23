import numpy as np

def test(arr0, var0):
    return np.where(arr0 > var0, var0, arr0)

