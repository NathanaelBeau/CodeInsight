import numpy as np

def test(arr0):
    return arr0[np.argsort(arr0[:, 1])]

