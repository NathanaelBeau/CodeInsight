import pandas as pd

def test(df, var0):
    result = df.groupby(var0, as_index=False).head(1).reset_index(drop=True)
    return result
