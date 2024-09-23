import numpy as np
def test(arr0):
    return np.count_nonzero(~np.isnan(arr0))

