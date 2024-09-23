import numpy as np

def test(arr0, var0):
    format_func = np.vectorize(lambda x: var0.format(x))
    return format_func(arr0)
