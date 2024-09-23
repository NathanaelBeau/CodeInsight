import pandas as pd

def test(df: pd.DataFrame) -> list:
    return df['a'].tolist()
