import pandas as pd

def test(df0, df1):
    merged = pd.merge(df0, df1, on=list(df0.columns), how='inner')
    return merged

