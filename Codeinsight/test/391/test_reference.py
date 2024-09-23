import pandas as pd

def test(df: pd.DataFrame) -> list:
    return list(df['a'].values)


