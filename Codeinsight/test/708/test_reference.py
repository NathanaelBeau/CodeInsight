import pandas as pd

def test(df0: pd.DataFrame):
    return df0.replace('-', None)

