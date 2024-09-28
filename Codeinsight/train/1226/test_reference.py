import numpy as np
def test(arr0):
    return np.argmax(np.bincount(arr0))
