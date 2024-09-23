import pandas as pd

def test(df0, col_name0, value0):
    return (df0[col_name0] == value0).sum()

