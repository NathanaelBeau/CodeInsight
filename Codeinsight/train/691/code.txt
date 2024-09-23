import numpy as np

def test(arr0):
    return (np.arange(arr0.size) % 2) * (arr0 + np.array([-1, 0, 1])[:, None])
