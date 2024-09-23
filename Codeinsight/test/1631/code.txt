import numpy as np
def test(arr0):
    return np.unravel_index(np.argmin(arr0), arr0.shape)
