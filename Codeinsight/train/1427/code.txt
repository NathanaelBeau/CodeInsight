import numpy as np

def test(arr0, arr1):
    arr0_reshaped = arr0[:, np.newaxis]
    arr1_reshaped = arr1[np.newaxis, :]
    result = np.dot(arr0_reshaped, arr1_reshaped)
    return result
