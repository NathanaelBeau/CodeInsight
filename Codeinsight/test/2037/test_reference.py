import pandas as pd

def test(df0, col_name, value0):
    return value0 in df0[col_name].unique()

