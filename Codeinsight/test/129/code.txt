import numpy as np

def test(var0):
    return (var0[:,1:] == var0[:,:-1]).all()