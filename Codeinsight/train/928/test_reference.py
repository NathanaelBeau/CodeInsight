import pandas as pd

def test(df0, df1):
    return df0.append(df1, ignore_index=True)

