import pandas as pd

def test(df0, str0):
    return df0.loc[:, ~df0.columns.str.endswith(str0)]
