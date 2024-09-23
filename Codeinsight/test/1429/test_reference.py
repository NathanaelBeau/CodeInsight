import pandas as pd

def test(df0, str0, var0):
    return df0.set_index(str0).rolling(var0).mean().reset_index()

