import numpy as np
def test(mat0, mat1):
    return np.sum(mat0 * mat1.T, axis=1)
