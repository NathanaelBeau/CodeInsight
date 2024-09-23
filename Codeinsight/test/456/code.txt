import numpy as np
def test(arr0):
    return np.where(np.isneginf(arr0), 0, arr0)
