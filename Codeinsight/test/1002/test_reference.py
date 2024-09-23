import numpy as np

def test(arr0, var0, var1):
    indices = list(range(0, arr0.shape[var1], var0))
    return np.delete(arr0, indices, axis=var1)

