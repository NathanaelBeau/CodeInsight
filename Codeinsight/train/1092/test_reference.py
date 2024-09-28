import pandas as pd
import numpy as np

def test(df0):
    df0.replace([np.inf, -np.inf], np.nan, inplace=True)
    return df0
