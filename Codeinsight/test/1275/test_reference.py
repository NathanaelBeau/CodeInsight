import numpy as np

def test(arr0):
    return np.concatenate((arr0[:2], arr0[-2:]))
