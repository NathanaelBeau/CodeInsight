import pandas as pd

def test(df0):
    return df0.loc[df0.index.repeat(5)].reset_index(drop=True)
