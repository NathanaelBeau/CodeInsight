import pandas as pd
import numpy as np

def test(df0):
    return np.array([tuple(x) for x in df0.values])
