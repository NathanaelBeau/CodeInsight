import pandas as pd

def test(df0, col0):
    df0[col0] = pd.factorize(df0[col0])[0]
    return df0