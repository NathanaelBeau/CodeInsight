import pandas as pd

def test(df0, col0):
    return df0.groupby(col0).mean()