import pandas as pd

def test(df0, var0):
    return df0.groupby(var0).filter(lambda x: len(x) > 1).reset_index(drop=True)
