import numpy as np

def test(arr0, arr1):
    return np.linalg.norm(arr0 - arr1, axis=-1)



