import pandas as pd

def test(df0, var0, var1):
    cols = df0.filter(regex=var0).columns
    df0[cols] = df0[cols] / var1
    return df0
