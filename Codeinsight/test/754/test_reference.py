import numpy as np
def test(mat0, mat1):
    return np.einsum('ij,ji->i', mat0, mat1)