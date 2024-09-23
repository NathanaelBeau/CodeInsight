import pandas as pd

def test(df0):
    df0.sort_values(['col0', 'col1'], ascending=[True, False], inplace=True)
    return df0

