import pandas as pd

def test(df0):
    return df0.apply(pd.value_counts).fillna(0)
