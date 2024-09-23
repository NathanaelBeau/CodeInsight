import numpy as np

def test(var0):
    min_indices = np.where(var0 == var0.min())
    return min_indices
