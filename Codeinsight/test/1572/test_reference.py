import numpy as np

def test(np_array: np.ndarray, value: float) -> np.ndarray:
    return np.argwhere(np_array == value)

