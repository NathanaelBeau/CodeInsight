import numpy as np
def test(arr0):
    _, idx = np.unique(arr0, return_index=True)
    return arr0[np.sort(idx)]

