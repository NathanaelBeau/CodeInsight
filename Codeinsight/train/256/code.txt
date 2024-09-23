import numpy as np

def test(old_set: np.ndarray, new_set: np.ndarray) -> np.ndarray:
    return (old_set + new_set) / 2
