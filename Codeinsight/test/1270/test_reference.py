import numpy as np

def test(arr0, var0):
    elements_to_remove = arr0[var0]
    arr0 = arr0[~np.isin(arr0, elements_to_remove)]
    return arr0

