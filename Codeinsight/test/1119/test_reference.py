import numpy as np
def test(lst0):
    return [[(lst0[i] - j if i % 2 else 0) for i in range(len(lst0))] for j in (1, 0, -1)]