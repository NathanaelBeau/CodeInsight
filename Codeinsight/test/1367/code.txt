import numpy as np
def test(arr0, arr1):
    return np.may_share_memory(arr0, arr1)
