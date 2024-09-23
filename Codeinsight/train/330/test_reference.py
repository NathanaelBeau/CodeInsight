import numpy as np
def test(mat0, var0, var1):
    return mat0.transpose(*[var1 if i == var0 else var0 if i == var1 else i for i in range(mat0.ndim)])

