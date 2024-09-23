import pandas as pd
import numpy as np

def test(df0):
    return np.where(df0.isnull().any(axis=1))[0].tolist()

