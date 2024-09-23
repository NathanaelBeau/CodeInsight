import pandas as pd

def test(df0, var0, var1):
    df0.columns = [var1 if x == var0 else x for x in df0.columns]
    return df0
