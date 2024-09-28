import pandas as pd



def test(df0):
    return df0.subtract(df0.min()).div(df0.max() - df0.min())

