import numpy as np
def test(arr0):
    return np.sum(~np.isnan(arr0))
