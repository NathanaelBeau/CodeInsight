import numpy as np

def test(str0):
    return np.frombuffer(str0, dtype='<f4')
