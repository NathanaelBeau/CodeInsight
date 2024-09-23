import pandas as pd

def test(df0, column_name0):
    df0[column_name0] = df0[column_name0].astype(int)
    return df0