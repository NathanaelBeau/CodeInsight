import pandas as pd

def test(df0, var0, var1):
    return df0.rename(columns={df0.columns[var0]: var1})
