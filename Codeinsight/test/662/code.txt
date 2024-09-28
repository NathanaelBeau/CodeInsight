import numpy as np

def test(var0):
    np.add.at(var0, np.array([1, 2, 2, 1, 3]), np.array([1, 1, 1, 1, 1]))
    return var0


