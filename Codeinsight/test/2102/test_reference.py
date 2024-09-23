import numpy as np
def test(var0, str0):
    if str0 == "upper":
        return np.triu(var0)
    elif str0 == "lower":
        return np.tril(var0)
    else:
        raise ValueError("str0 must be 'upper' or 'lower'")

