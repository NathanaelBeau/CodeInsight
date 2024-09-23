import pandas as pd

def test(df0):
    return df0.apply(dict, axis=1).tolist()

