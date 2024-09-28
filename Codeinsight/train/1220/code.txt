import numpy as np

def test(var0):
    indices = np.argwhere(var0)
    return [(i, j) for i, j in indices]