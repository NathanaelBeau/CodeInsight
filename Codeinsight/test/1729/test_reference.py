import pandas as pd

def test(df0, df1, df2):
    return df0.merge(df1, on='name').merge(df2, on='name')

