import pandas as pd

def test(df0, str0):
    df2 = df0.drop([col for col in df0.columns if str0 in col], axis=1)
    return df2
