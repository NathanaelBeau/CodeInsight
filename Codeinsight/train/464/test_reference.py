import pandas as pd

def test(df0, var0):
    return df0.nsmallest(n=len(df0), columns=var0)
