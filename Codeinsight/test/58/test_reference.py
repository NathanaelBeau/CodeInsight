import numpy as np
def test(arr0, var0):
    arr0[arr0 > var0] = 0
    return arr0
