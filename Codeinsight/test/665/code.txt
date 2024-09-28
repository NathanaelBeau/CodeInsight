import numpy as np

def test(var0):
    min_value = var0.min()
    min_indices = np.argwhere(var0 == min_value)
    return min_indices.flatten()
