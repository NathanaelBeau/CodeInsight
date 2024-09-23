import numpy as np
def test(arr0):
    return [arr0[:, i] for i in range(arr0.shape[1])]

