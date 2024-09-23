import pandas as pd
def test(df0, col0):
    df0['compared'] = df0[col0].eq(df0[col0].shift())
    return df0

