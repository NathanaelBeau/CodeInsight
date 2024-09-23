import numpy as np

def test(var0: np.ndarray) -> np.ndarray:
    return var0.T.reshape(-1, 2, 2).swapaxes(1, 2).reshape(-1, 2)

