import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return df0.loc[:, ['x', 'y', 'a', 'b']]
