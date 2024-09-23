import pandas as pd

def test(df0):
    return df0.loc[:, (df0 != 0).any(axis=0)]