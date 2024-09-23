import numpy as np
def test(arr0, var0):
    return np.repeat(arr0[:, :, np.newaxis], var0, axis=2)

