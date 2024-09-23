import numpy as np

def test(arr0: List[List[float]]):
    x = np.array(arr0)
    return np.int_(x).tolist()
