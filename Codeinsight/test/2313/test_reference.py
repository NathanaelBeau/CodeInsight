import pandas as pd

def test(df0, dict0):
    df0.index = df0.index.to_series().replace(dict0)
    return df0

