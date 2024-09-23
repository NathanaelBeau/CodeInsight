import numpy as np
def test(lst0, var0):
    lst0 = np.asarray(lst0)
    idx = (np.abs(lst0 - var0)).argmin()
    return lst0[idx]

