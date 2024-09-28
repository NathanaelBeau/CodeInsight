import numpy as np

def test(arr0):
    return np.split(arr0, np.where(np.diff(arr0) != 1)[0] + 1)