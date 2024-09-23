import pandas as pd

def test(df0: pd.DataFrame, var0: str, var1: str, var2: str) -> pd.DataFrame:
    df0[var0] = df0[var1] / df0[var2]
    return df0

