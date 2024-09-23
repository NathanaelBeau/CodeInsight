import numpy as np
def test(arr0):
    col_mean = np.nanmean(arr0, axis=0)
    inds = np.where(np.isnan(arr0))
    arr0[inds] = np.take(col_mean, inds[1])
    return arr0

