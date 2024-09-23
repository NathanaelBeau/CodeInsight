import pandas as pd
import numpy as np

def test(df0, lst0):
    df0[lst0] = pd.DataFrame([[np.nan] * len(lst0)], index=df0.index)
    return df0

