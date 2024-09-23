import numpy as np
def test(arr0, var0, var1):
    return np.where(arr0 == var0, var1, arr0)
