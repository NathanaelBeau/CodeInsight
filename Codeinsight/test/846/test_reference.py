import pandas as pd

def test(df0):
    df0.drop(columns=[col for col in df0.columns if (df0[col] == 0).all()], inplace=True)
    return df0

