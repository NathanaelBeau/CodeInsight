import pandas as pd
import numpy as np

def test(df0, lst0):
    for col in lst0:
        df0[col] = np.nan
    return df0

