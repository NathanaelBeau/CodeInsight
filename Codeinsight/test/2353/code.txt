import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return df0.loc[:, df0.max() <= 0]
