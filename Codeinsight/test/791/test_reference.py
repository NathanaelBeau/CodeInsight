import numpy as np
def test(mat0, part='upper'):
    if part == 'upper':
        return np.triu(mat0)
    elif part == 'lower':
        return np.tril(mat0)
