import pandas as pd

def test(df0) -> pd.Series:
    return df0.iloc[:, -1]

