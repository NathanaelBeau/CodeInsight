import numpy as np
def test(mat0, val0):
    return len(np.where(mat0 < val0)[0])
