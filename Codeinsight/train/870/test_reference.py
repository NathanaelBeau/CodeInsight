import numpy as np
def test(arr0, arr1):
    return np.array(np.meshgrid(arr0, arr1)).T.reshape(-1, 2)

