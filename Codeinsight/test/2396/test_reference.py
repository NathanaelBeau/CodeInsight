import numpy as np
def test(arr0, lst0, lst1):
    rows_to_keep = [i for i in range(arr0.shape[0]) if i not in lst0]
    cols_to_keep = [i for i in range(arr0.shape[1]) if i not in lst1]
    
    return arr0[np.ix_(rows_to_keep, cols_to_keep)]
