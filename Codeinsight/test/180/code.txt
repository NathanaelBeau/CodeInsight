import pandas as pd

def test(df0, str2, str0, str1):
    df0.loc[df0[str2] == str0, str2] = str1
    return df0
