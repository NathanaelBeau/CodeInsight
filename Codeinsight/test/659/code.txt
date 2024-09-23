import numpy as np
def test(arr0, lst0):
    return np.array([arr0[i, idx] for i, idx in enumerate(lst0)])
