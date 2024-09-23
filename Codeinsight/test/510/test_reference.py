import pandas as pd

def test(df0, str0):
    return df0.loc[:, (slice(None), str0)]

