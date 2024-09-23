import pandas as pd

def test(df0, col0):
    return pd.Series([len(lst) for lst in df0[col0]])

