import numpy as np
def test(mat0, columns_to_delete):
    return np.delete(mat0, columns_to_delete, axis=1)

