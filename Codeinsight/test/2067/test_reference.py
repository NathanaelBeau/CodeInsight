import numpy as np

def test(arr0):
    return arr0[np.lexsort((arr0[:, 0], arr0[:, 1]))]

