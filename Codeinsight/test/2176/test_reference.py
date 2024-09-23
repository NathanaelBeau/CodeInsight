import pandas as pd

def test(df: pd.DataFrame, lst0: list, lst1: list) -> pd.DataFrame:
    return df.reindex(columns=lst1)
