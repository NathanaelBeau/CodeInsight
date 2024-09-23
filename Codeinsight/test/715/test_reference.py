import numpy as np

def test(x: np.ndarray, var0: int) -> np.ndarray:
    return np.delete(x, var0, axis=0)
