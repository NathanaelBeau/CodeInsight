import numpy as np
from scipy.signal import argrelextrema
def test(arr0):
    maxima = argrelextrema(arr0, np.greater)[0]
    minima = argrelextrema(arr0, np.less)[0]
    return maxima, minima

