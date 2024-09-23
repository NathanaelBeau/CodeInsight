import numpy as np

def test(mat0):
    return mat0 / mat0.sum(axis=1)[:, np.newaxis]

