import pandas as pd

def test(df0):
    df0.fillna(df0.mean(), inplace=True)
    return df0