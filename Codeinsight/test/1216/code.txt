import pandas as pd

def test(df0, col0, str0):
    return df0[df0[col0].str.startswith(str0)].reset_index(drop=True)
