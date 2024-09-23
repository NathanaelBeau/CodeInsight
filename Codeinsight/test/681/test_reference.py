import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return df0.groupby(df0.index).sum()
