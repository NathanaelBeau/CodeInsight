import numpy as np

def test(data: np.ndarray) -> int:
    return np.count_nonzero(~np.isnan(data))
