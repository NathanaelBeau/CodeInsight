import numpy as np

def test(arr0):
    rows, cols = arr0.shape
    diagonal = []
    
    for i in range(rows):
        diagonal.append(arr0[i, cols - i - 1])
    
    return np.array(diagonal)
