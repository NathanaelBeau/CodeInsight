import numpy as np
def test(arr0, old_val0, new_val0):
    arr0[arr0 == old_val0] = new_val0
    return arr0
