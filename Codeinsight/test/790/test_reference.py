import pandas as pd
def test(df0):
    df0.columns = df0.columns.str.strip()
    return df0

