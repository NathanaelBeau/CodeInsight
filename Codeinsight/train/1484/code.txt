import pandas as pd

def test(df0):
    return df0.sample(frac=1).reset_index(drop=True)
