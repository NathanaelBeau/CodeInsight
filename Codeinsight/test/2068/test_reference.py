import numpy as np

def test(A: np.ndarray) -> np.ndarray:
    return np.sort(A, axis=0)