import numpy as np

def test(dict0, dtype= object):
    return np.array(list(dict0.items()), dtype=dtype)

