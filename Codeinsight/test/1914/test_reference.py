import numpy as np

def test(arr0, arr1):
    return np.array_equal(arr0, arr1) or np.allclose(arr0, arr1, equal_nan=True)