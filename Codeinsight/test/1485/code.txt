import numpy as np
def test(matrix0):
    return np.array([np.linalg.norm(row) for row in matrix0])
