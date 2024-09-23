import pandas as pd

def test(df0, var0):
    return df0[df0.duplicated(subset=var0, keep=False)]
