from operator import itemgetter
import numpy as np

def test(arr0, sort_column):
    sorted_array = sorted(arr0.tolist(), key=itemgetter(sort_column))
    return np.array(sorted_array)
