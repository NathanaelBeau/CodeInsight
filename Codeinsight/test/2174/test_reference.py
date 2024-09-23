import pandas as pd

def test(df0, df1):
    return df0.merge(df1, how='outer').drop_duplicates().reset_index(drop=True)

