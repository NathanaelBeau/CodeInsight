import pandas as pd

def test(df0, var0, var1, var2):
    return df0.pivot(index=var0, columns=var1, values=var2)

