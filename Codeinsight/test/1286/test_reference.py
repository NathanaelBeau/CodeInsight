import pandas as pd

def test(df0, column_name0, decimals0):
    df0[column_name0] = df0[column_name0].round(decimals0)
    return df0

