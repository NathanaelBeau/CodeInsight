import pandas as pd

def test(df, var0):
    result = df[df.groupby(var0).cumcount() == 0].reset_index(drop=True)
    return result
