import numpy as np
def test(arr0):
    return np.where((arr0 == (0,1)).all(axis=1))
