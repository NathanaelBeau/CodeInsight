import pandas as pd

def test(df0, var0):
    return {key: group.reset_index(drop=True) for key, group in df0.groupby(var0)}

