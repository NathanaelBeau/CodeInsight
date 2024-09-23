import numpy as np
def test(arr0, var0):
    mask = np.arange(arr0.shape[0]) != var0
    return arr0[mask]

