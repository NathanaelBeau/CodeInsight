import numpy as np

def test(arr0, arr1):
    arr0_reshaped = arr0[:, None]
    arr1_reshaped = arr1[None, :]
    result = np.dot(arr0_reshaped, arr1_reshaped)
    return result
