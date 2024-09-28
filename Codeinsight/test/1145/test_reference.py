import numpy as np

def test(arr0, arr1):
    return np.insert(arr1, obj=range(arr0.shape[0]), values=arr0)
