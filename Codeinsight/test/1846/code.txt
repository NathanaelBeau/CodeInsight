import numpy as np

def test(lst0):
    la = len(lst0)
    arr = np.array(np.meshgrid(*lst0)).T.reshape(-1, la)
    arr = [tuple(map(lambda x: x.item() if isinstance(x, np.generic) else x, row)) for row in arr]
    return arr