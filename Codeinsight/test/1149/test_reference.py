import pandas as pd

def test(df0, lst0):
    cols_to_include = [col for col in df0.columns if col not in lst0]
    return df0[cols_to_include]

