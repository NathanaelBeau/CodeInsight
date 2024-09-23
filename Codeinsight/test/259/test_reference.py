import numpy as np

def test(x, var0):
    return np.vstack((x[:var0], x[var0+1:]))
