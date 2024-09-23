import numpy as np
def test(mat0):
    return np.array([np.linalg.norm(row) for row in mat0])
