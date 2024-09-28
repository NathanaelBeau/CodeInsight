import pandas as pd

def test(df0, df1):
    return pd.concat([df0, df1]).sort_values(by='y').reset_index(drop=True)
