import pandas as pd

def test(df0, df1):
    return df0.merge(df1, left_index=True, right_index=True)
