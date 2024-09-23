import numpy as np
def test(arr0, var0):
    return np.partition(arr0, -var0)[-var0:]

