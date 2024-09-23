import pandas as pd

def test(df0, func, var0):
    return df0.apply(func, axis=var0)

