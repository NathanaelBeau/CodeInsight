import numpy as np

def test(str0):
    chars = np.array(list(str0))
    reversed_chars = np.flip(chars)
    return ''.join(reversed_chars)
