import pandas as pd
def test(df0, colA, some_value, colB, new_value):
    df0.loc[df0[colA] == some_value, colB] = new_value
    return df0
