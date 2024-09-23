import numpy as np

def test(arr0: np.ndarray) -> np.ndarray:
    return np.cumsum(arr0[::-1])[::-1]
