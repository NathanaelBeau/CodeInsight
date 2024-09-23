import pandas as pd

def test(df0):
    return df0.sort_values(['A', 'B'], ascending=[True, False]).drop_duplicates(subset='A', keep='first')
