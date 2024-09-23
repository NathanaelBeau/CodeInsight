import pandas as pd

def test(df0):
    return pd.get_dummies(df0, dtype=int)
