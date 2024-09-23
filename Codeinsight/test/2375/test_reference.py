import numpy as np
def test(arr0):
    arr0[arr0 == -np.inf] = 0
    return arr0

