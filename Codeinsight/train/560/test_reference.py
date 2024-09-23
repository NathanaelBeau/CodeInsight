import numpy as np

def test(dict0, dtype= object):
    keys = list(dict0.keys())
    values = list(dict0.values())
    data = list(zip(keys, values))
    return np.array(data, dtype=dtype)
