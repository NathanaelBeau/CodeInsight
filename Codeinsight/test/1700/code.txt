import numpy as np
def test(mat0, mat1):
    return np.sum(mat0 * mat1, axis=1)