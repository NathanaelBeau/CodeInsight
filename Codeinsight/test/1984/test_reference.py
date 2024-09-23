import pandas as pd

def test(var0, df0):
    cols = pd.MultiIndex.from_product([[var0], df0.columns])
    df_copy = df0.copy()
    df_copy.columns = cols
    return df_copy

