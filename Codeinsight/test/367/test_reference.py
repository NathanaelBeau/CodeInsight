import pandas as pd

def test(df0, lst0):
    return df0.drop_duplicates(subset=lst0)

