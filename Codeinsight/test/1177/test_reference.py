import numpy as np

def test(arr0, n0):
    q, r = divmod(len(arr0), n0)
    indices = np.arange(n0+1) * q + np.minimum(np.arange(n0+1), r)
    return [arr0[indices[i]:indices[i+1]] for i in range(n0)]
