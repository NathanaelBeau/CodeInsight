import numpy as np
def test(arr0):
    count = 0
    for element in arr0:
        if not np.isnan(element):
            count += 1
    return count

