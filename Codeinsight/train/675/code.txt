import pandas as pd


def test(df0, lst0):
    df0.drop(columns=lst0, axis=1, inplace=True)
    return df0
