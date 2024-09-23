import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    df0['A_perc'] = df0['A'] / df0['sum']
    return df0

