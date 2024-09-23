import numpy as np
def test(arr0, arr1):
    return arr0.base is arr1 or arr1.base is arr0 or arr0 is arr1

