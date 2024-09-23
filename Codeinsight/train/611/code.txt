import pandas as pd
import numpy as np

def test(df0):
    return np.sqrt(np.square(df0).sum(axis=1))