import numpy as np
def test(arr0):
    nans, x = np.isnan(arr0), lambda z: z.nonzero()[0]
    arr0[nans] = np.interp(x(nans), x(~nans), arr0[~nans])
    return arr0

