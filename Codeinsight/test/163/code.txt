import pandas as pd

def test(df: pd.DataFrame, key_columns: str) -> pd.DataFrame:
    return df.groupby(key_columns).size().reset_index(name='counts')
