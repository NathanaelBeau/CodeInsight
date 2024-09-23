import numpy as np

def test(arr0):
    mask = np.zeros(arr0.shape[0], dtype=bool)
    mask[:2] = True
    mask[-2:] = True
    return arr0[mask]
