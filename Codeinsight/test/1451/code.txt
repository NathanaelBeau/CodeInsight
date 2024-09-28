import pandas as pd

def test(df0, var0):
    return df0[[col for col in df0 if col != var0]]
