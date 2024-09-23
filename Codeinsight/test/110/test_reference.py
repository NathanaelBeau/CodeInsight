import numpy as np

def test(arr0):
    return (arr0 - arr0.min()) / (arr0.max() - arr0.min())

