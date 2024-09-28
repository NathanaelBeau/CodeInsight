import numpy as np

def test(arr0):
    rows, cols = arr0.shape
    diagonal = [arr0[i, cols - i - 1] for i in range(rows)]
    
    return np.array(diagonal)
