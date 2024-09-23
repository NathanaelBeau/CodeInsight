import pandas as pd

def test(df0, var0, var1):
    return df0.sort_values(var0, ascending=var1)