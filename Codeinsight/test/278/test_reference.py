import pandas as pd
def test(df0):
    return df0.isnull().sum() / len(df0) * 100

