import numpy as np

def test(arr0, var0):
    return np.delete(arr0, np.where(arr0 == var0))
