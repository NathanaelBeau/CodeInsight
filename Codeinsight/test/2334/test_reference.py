import numpy as np


def test(arr0):
    return sum(~np.isnan(arr0))

