import pandas as pd

def test(df1, df2):
    return pd.concat([df1, df2], axis=1)

