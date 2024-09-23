import numpy as np
def test(arr0):
    means = np.nanmean(arr0, axis=0)
    return np.where(np.isnan(arr0), means, arr0)
