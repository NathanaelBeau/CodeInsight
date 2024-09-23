import numpy as np
def test(arr0, var0):
    return np.tile(arr0[:, :, np.newaxis], (1, 1, var0))

