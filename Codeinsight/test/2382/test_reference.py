import numpy as np

def test(np_array: np.ndarray, value: float) -> tuple:
    return np.where(np_array == value)
