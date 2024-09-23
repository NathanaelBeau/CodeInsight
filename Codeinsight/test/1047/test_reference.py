import numpy as np
def test(arr0, var0):
    return arr0[np.arange(arr0.size) != var0]

