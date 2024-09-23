import numpy as np
def test(arr0):
    return arr0 / arr0.sum(axis=1)[:, np.newaxis]
