import pandas as pd

def test(df0, df1):
    return pd.concat([df0, df1]).drop_duplicates().reset_index(drop=True)
