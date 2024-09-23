import numpy as np

def test(arr0):
    mask = np.all(np.isfinite(arr0), axis=1)
    return arr0[mask]

