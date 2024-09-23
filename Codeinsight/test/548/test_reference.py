import pandas as pd

def test(df0):
    df0.columns = [' '.join(col).strip() for col in df0.columns.values]
    return df0

