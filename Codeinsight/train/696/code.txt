import numpy as np

def test(arr0, var0):
    n, m = arr0.shape
    for i in range(min(n, m)):
        arr0[i, i] = var0
    return arr0
