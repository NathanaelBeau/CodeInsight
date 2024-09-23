import pandas as pd

def test(df0, col0, col1):
    return pd.to_datetime(df0[col0] + ' ' + df0[col1])