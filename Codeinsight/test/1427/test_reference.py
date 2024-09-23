import numpy as np

def test(arr0):
    return np.array(sorted(arr0, key=lambda row: tuple(row)))
