import numpy as np

def test(var0: np.ndarray):
    r = var0.T.reshape(-1, 2, 2)
    s = r.swapaxes(1, 2)
    t = s.reshape(-1, 2)
    return t

