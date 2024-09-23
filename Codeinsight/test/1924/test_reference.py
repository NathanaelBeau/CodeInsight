import numpy as np
def test(arr0):
    arr0[np.isnan(arr0)] = 0
    return arr0

