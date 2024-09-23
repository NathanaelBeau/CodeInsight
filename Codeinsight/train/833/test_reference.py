import pandas as pd

def test(df0, index_name0):
    return df0.reset_index(drop=True).rename_axis(index_name0)
