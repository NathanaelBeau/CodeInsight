import pandas as pd

def test(var0, df0):
    df_copy = df0.copy()
    df_copy.columns = pd.MultiIndex(levels=[[var0], df0.columns],
                                    codes=[[0]*len(df0.columns), list(range(len(df0.columns)))])
    return df_copy

