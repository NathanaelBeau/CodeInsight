import pandas as pd

def test(df0, column_name0, some_value0):
    return df0.index[df0[column_name0] == some_value0].tolist()[0]

