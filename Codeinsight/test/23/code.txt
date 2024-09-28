import numpy as np
def test(arr0):
    return np.argwhere((arr0 == [0, 1]).all(axis=1)).flatten()
