import numpy as np
def test(matrix0, vec0):
    return matrix0 - vec0[:, np.newaxis]

