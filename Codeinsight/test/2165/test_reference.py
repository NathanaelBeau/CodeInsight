import numpy as np
def test(arr0, var0):
    shape = arr0.shape[:-1] + (arr0.shape[-1] - var0 + 1, var0)
    strides = arr0.strides + (arr0.strides[-1],)
    return np.lib.stride_tricks.as_strided(arr0, shape=shape, strides=strides)
