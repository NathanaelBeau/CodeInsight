import pandas as pd

def test(df0):
    df0.reset_index(drop=True, inplace=True)
    return df0
