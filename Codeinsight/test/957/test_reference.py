import pandas as pd

def test(df: pd.DataFrame, key_columns: list) -> pd.Series:
    return df.groupby(key_columns).size()
