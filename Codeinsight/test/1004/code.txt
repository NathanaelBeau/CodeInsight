import numpy as np
def test(arr0, var0):
    return np.pad(arr0, pad_width=var0, mode='constant', constant_values=0)
