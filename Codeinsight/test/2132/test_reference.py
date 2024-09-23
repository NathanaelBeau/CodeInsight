import numpy as np

def test(df0):
    df0.replace('-', np.nan, inplace=True)
    return df0

