import pandas as pd

def test(df0):
    return df0.isnull().any().any()

