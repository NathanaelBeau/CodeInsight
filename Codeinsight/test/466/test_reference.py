import pandas as pd

def test(df0, start_column0, end_column0):
    return df0.loc[:, start_column0:end_column0]

