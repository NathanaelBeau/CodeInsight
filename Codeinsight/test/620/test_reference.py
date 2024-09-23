import numpy as np
def test(arr0):
    norm = np.sqrt(np.sum(arr0**2))
    return arr0 / norm

