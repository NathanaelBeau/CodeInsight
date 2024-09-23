import pandas as pd
def test(df0, str0, str1):
    df0.set_index([str0, str1], inplace=True)
    return df0

