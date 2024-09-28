import numpy as np

def test(arr0, arr1):
    # Get the sorted indices of arr0
    sorted_indices = np.argsort(arr0)
    
    # Use these indices to sort both arr0 and arr1
    sorted_arr0 = arr0[sorted_indices]
    sorted_arr1 = arr1[sorted_indices]
    
    return sorted_arr0, sorted_arr1