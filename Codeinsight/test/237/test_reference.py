import numpy as np

def test(var0, var1):
    return (var0 == var1[:, None]).argmax(1)
