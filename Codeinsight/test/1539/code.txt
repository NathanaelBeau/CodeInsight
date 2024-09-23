from itertools import islice
import numpy as np

def test(lst0, window_size=2):
    lst0 = np.array(lst0)
    weights = np.ones(window_size) / window_size
    moving_averages = np.convolve(lst0, weights, mode='valid')
    return moving_averages.tolist()