import pandas as pd
def test(df0, column, value):
    df0.insert(df0.shape[1], column, value)
    return df0