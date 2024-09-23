import pandas as pd

def test(df: pd.DataFrame, lst0: list, lst1: list) -> pd.DataFrame:
    # Assuming lst1 contains the desired order of the columns from lst0
    return df[lst1]

