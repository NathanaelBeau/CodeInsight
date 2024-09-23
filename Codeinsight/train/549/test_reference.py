import numpy as np

def test(var0):
    sliced = np.hstack(var0[:, 3:5])
    return sliced