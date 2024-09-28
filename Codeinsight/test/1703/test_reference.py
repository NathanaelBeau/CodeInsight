import pandas as pd
def test(df0):
    return df0.sort_values('C').drop_duplicates(subset=['A', 'B'], keep='last')
