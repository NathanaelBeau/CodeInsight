import pandas as pd

def test(df0, str0, str1):
    df1 = df0.groupby(str0, as_index=False)[str1].sum()
    return df1


