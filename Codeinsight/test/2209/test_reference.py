import numpy as np
def test(lst0, lst1):
    result = np.zeros_like(np.outer(lst0[0], lst1[0]))
    for i in range(len(lst0)):
        result += np.outer(lst0[i], lst1[i])
    return result
