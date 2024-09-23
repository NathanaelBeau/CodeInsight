import numpy as np
def test(arr0, row0):
    return (arr0 == row0).all(axis=1).any()

