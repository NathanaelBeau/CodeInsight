import numpy as np

def test(arr0, row0):
    return any(np.array_equal(x, row0) for x in arr0)
