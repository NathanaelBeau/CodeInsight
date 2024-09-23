import numpy as np

def test(arr0):
    n = len(arr0)
    num_rows = (n + 1) // 2
    arr2d = np.zeros((num_rows, 2), dtype=arr0.dtype)
    arr2d[:, 0] = arr0[::2]
    arr2d[:, 1] = arr0[1::2]
    return arr2d