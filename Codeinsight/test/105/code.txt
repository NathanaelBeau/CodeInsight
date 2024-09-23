import numpy as np

def test(vec0, num_times0, axis0=0):
    if axis0 == 0:
        return np.tile(vec0, (num_times0, 1))
    else:
        return np.tile(vec0, (1, num_times0))
