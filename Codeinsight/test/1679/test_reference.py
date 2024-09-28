import pandas as pd

def test(df0):
    df0['grade'] = df0['grade'].astype(float).astype(int)
    return df0
