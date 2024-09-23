import numpy as np
def test(arr0, lst0):
    return [any(x == y for y in lst0) for x in arr0]
