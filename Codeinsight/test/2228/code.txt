import pandas as pd
def test(df0, var0, var1):
    idx = df0.groupby(var0)[var1].idxmax()
    return df0.loc[idx].reset_index(drop=True)
