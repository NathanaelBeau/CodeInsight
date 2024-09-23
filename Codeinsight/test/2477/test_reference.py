import numpy as np
def test(arr0, vec0):
    return arr0 / vec0[:, np.newaxis]
