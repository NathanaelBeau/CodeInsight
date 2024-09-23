import numpy as np
def test(mat0, columns_to_delete):
    return mat0[:, [i for i in range(mat0.shape[1]) if i not in columns_to_delete]]
