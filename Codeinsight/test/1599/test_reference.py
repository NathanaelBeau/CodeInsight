import numpy as np

def test(arr0, arr1):
    c = np.empty((arr0.size + arr1.size,), dtype=arr0.dtype)
    c[0::2] = arr0
    c[1::2] = arr1
    return c

