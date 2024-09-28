import numpy as np

def test(arr0, sort_columns):
    # Use lexsort to get the indices for sorting
    # Reverse the sort_columns for lexsort since it sorts in reverse order
    indices = np.lexsort(tuple(arr0[:, col] for col in reversed(sort_columns)))
    return arr0[indices]