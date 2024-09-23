import numpy as np
def test(arr0, arr1):
    sorter = np.argsort(arr1)
    return arr0[sorter]