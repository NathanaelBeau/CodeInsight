import numpy as np
def test(arr0, item0):
    unique, counts = np.unique(arr0, return_counts=True)
    item_index = np.where(unique == item0)
    return counts[item_index][0] if item_index[0].size > 0 else 0

