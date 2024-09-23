import numpy as np

def test(shape0):
    matrix = np.empty(shape0)
    matrix[:] = np.nan
    return matrix
