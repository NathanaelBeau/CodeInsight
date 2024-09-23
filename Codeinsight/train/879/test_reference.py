import pandas as pd

def test(df0, var0):
    df0[['col0', 'col1']] = df0[var0].apply(pd.Series)
    return df0.drop(columns=[var0])

