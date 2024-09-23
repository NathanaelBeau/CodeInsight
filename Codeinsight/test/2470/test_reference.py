import numpy as np

def test(arr0):
    return np.diag(np.rot90(arr0))
