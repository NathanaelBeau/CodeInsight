import pandas as pd

def test(df0, df1, var0):
    merged = pd.merge(df0, df1, on=var0, how='inner')
    selected_cols = var0
    return merged[var0]
