import pandas as pd

def test(df0, lst0):
    df0 = df0.assign(sum=df0[lst0].sum(axis=1))
    return df0
