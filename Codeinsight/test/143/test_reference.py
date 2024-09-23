import numpy as np

def test(arr0: np.ndarray, arr1: np.ndarray) -> np.ndarray:
    return np.concatenate((arr0, arr1))
