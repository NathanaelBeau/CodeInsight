import numpy as np

def test(arr0):
    y = np.vstack([arr0 + i for i in [-1, 0, 1]])
    y[:, ::2] = 0
    return y