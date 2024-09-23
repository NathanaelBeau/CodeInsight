import numpy as np

def test(arr0, var0):
    a = np.zeros((arr0.shape[0], var0))
    a[np.arange(arr0.shape[0]), arr0] = 1
    return a
