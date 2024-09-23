import numpy as np
def test(arr0, var0, var1):
    arr0[arr0 == var0] = var1
    return arr0

