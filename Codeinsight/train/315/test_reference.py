import numpy as np
def test(arr0):
    # Add a sentinel value at the end
    arr = np.r_[arr0, arr0[-1] + 1]
    idx = np.where(arr[:-1] != arr[1:])[0] + 1
    lengths = np.diff(np.r_[0, idx])
    return arr0[idx - 1], lengths

