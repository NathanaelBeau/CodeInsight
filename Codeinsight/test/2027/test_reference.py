import pandas as pd

def test(df0, col_name, value0):
    return (df0[col_name] == value0).any()

