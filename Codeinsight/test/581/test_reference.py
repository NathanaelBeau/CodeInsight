import numpy as np

def test(arr0):
    indices = np.take([0, 1, -2, -1], np.arange(4))
    return np.take(arr0, indices, axis=0)
