import numpy as np

def test(arr0, var0):
    return np.quantile(arr0, var0 / 100)

