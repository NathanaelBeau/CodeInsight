import numpy as np

def test(arr0, var0):
    return arr0[arr0[:,var0].argsort()]

