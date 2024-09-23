import numpy as np
def test(lst0, var0):
    one_hot = np.zeros((len(lst0), var0))
    one_hot[np.arange(len(lst0)), lst0] = 1
    return one_hot
