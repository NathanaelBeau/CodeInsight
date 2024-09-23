import pandas as pd
def test(df0, colA, some_value, colB, new_value):
    df0[colB] = df0.apply(lambda row: new_value if row[colA] == some_value else row[colB], axis=1)
    return df0

