import pandas as pd

def test(df0, var0):
    return [col for col in df0.columns if var0 in df0[col].values]
