import pandas as pd

def test(df0, var0):
    result = df0.groupby(var0, as_index=False).first()
    return result
