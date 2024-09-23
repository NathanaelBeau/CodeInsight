import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return df0.groupby(level=0, axis=0).sum()