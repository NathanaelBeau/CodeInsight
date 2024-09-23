import numpy as np

def test(arr0):
    return [dict(zip(arr0, row)) for row in arr0]
