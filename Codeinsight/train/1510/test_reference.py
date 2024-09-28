import numpy as np

def test(arr0):
    sorted_indices = np.argsort(arr0)
    nan_indices = np.where(np.isnan(arr0))[0]
    non_nan_indices = sorted_indices[~np.isin(sorted_indices, nan_indices)][::-1]
    sorted_indices[-len(nan_indices):] = nan_indices
    sorted_indices[:-len(nan_indices)] = non_nan_indices
    return arr0[sorted_indices]
