import pandas as pd

def test(df0, var0):
    return df0.nlargest(1, var0).iloc[0]
