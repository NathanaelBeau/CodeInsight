import numpy as np
def test(lst0, var0):
    return lst0.argsort()[-var0:][::-1]
