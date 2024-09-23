import numpy as np

def test(arr0):
    n = len(arr0)
    m = n // 2 + n % 2
    return np.array([arr0[i:i+2] for i in range(0, n, 2)])