import pandas as pd

def test(df0, var0='X'):
    return df0.filter(like=var0, axis=1)
