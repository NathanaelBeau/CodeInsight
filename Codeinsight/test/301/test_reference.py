import numpy as np

def test(var0):
    return [(i, j) for i in range(var0.shape[0]) for j in range(var0.shape[1]) if var0[i, j]]

