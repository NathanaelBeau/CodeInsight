import pandas as pd

def test(df0):
    result = df0.groupby(by=df0.columns.str.split("_").str[0], axis=1).mean()
    return result.astype(int, errors='ignore')