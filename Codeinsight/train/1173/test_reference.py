import numpy as np

def test(A: list, B: list) -> list:
    return list(np.where(np.isin(A, B))[0])