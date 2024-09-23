import numpy as np
def test(arr0):
    return np.where(arr0 < 0, 0, arr0)