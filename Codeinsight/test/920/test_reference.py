import numpy as np
def test(matrix0):
    return np.sqrt(np.einsum('ij,ij->i', matrix0, matrix0))

