import numpy as np

def test(arr0, var0):
    split = np.hsplit(arr0, arr0.shape[1])
    del split[var0]
    return np.column_stack(split)

