import pandas as pd

def test(df0):
    return df0.iloc[:, :].reset_index(drop=True)
