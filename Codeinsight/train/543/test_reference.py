import numpy as np

def test(arr0):
    return np.array(list(filter(lambda v: v == v, arr0)))