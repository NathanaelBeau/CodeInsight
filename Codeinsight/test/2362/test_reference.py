import pandas as pd

def test(df0, str0):
    df0[str0] = pd.to_datetime(df0[str0])
    return df0
