import pandas as pd

def test(df0, str0, var0):
    return df0.loc[df0[str0] == var0].reset_index(drop=True)[expected_output.columns]

