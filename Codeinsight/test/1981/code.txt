import pandas as pd

def test(str0, df0):
    return df0.isin([str0]).any().any()
