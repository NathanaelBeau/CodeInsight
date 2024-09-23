import pandas as pd

def test(df0):
    return df0.drop(df0.index[:3])
