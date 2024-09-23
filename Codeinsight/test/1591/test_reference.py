import pandas as pd
def test(df0):
    return df0.groupby(df0.columns, axis=1).sum()

