import numpy as np

def test(arr0, arr1):
    arr0_reshaped = arr0[:, None]
    result = arr0_reshaped * arr1
    return result

