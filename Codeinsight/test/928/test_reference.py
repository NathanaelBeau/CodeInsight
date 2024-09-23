import numpy as np

def test(arr0):
    column = arr0[:, 1]
    diff = np.diff(column)
    indices = np.where(diff)[0] + 1
    return indices
