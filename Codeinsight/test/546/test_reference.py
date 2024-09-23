import numpy as np
def test(arr0):
    return np.array2string(arr0, separator=', ', max_line_width=np.inf)[1:-1]

