import pandas as pd
def test(df0, str0):
    return df0[df0.columns.difference(df0.filter(like=str0).columns)]

