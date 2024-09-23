import pandas as pd
def test(df0):
    return df0.sort_values('C', ascending=False).drop_duplicates(subset=['A', 'B'], keep='first').sort_index()

