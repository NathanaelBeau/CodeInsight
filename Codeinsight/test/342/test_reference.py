import pandas as pd

def test(df0, index_name0):
    df0 = df0.reset_index(drop=True)
    df0.index.name = index_name0
    return df0