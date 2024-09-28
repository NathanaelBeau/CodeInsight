import pandas as pd

def test(df0, str0, var0):
    return df0[df0[str0].str.len() > var0]
