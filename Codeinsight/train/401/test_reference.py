import numpy as np

def test(data: np.ndarray) -> int:
    return data.size - np.isnan(data).sum()