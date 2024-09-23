import numpy as np
import pandas as pd

def test(df0, lst0, lst1):
    return pd.Series(np.mean(df0.loc[lst0, lst1].values, axis=0), index=lst1)

