import pandas as pd

def test(df0, var0):
    df0[var0] = pd.to_datetime(df0[var0])
    return df0
