import numpy as np
def test(arr0: np.ndarray):
    return arr0[arr0 != 0].min()
