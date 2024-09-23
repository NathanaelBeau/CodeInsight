import pandas as pd

def test(df: pd.DataFrame) -> pd.DataFrame:
    df.fillna(0.0, inplace=True)
    return df

