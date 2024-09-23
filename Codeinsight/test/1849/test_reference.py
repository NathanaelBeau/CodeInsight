import pandas as pd

def test(df0, col0):
    df0[['A', 'B']] = df0[col0].apply(pd.Series)
    return df0.drop(col0, axis=1)

