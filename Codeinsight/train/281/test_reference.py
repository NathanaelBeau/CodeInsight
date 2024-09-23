import pandas as pd

def test(df0, str0, var0, columns):
    return df0.loc[df0[str0] == var0].reset_index(drop=True)[columns]
