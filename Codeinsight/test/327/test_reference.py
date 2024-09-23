import pandas as pd

def test(df0):
    df0.columns = df0.columns.map(' '.join)
    return df0
