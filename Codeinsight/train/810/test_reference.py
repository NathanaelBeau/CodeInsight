import pandas as pd

def test(df0, var0='X'):
    return df0[[col for col in df0.columns if col.startswith(var0)]]

