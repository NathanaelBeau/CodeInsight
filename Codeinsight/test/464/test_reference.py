import pandas as pd

def test(df0, str0):
    return df0.groupby(str0).filter(lambda x: len(x) > 1).reset_index(drop=True)
