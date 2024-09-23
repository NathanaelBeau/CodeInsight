import pandas as pd

def test(df0):
    return [list(x) for x in df0.T.itertuples()]


