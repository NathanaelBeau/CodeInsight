import numpy as np

def test(arr0, var0):
    arr0[arr0 > var0] = var0
    return arr0

