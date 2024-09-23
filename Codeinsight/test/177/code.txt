import pandas as pd

def test(df0, var0, var1):
    if var1 == "column":
        return df0[var0].tolist()
    elif var1 == "row":
        return df0.iloc[var0].tolist()
