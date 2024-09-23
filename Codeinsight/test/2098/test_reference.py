import pandas as pd

def test(df0, var0, var1):
    if var1 == "column":
        return list(df0[var0])
    elif var1 == "row":
        return list(df0.iloc[var0])

