import numpy as np

def test(arr0):
    return np.compress(~np.isnan(arr0), arr0)
