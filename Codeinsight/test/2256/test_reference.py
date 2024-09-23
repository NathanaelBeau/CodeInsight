import numpy as np 

def test(arr0, var0, var1):
    return (arr0 - arr0.min()) * (var1 - var0) / (arr0.max() - arr0.min()) + var0

