import pandas as pd

def test(df1, df2, col0, var0, var1):
    df2[var0] = df2[col0].map(df1.set_index(var1)[var0])
    return df2
