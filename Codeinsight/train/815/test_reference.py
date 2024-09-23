import pandas as pd

def test(df0: pd.DataFrame):
    df0.columns = df0.iloc[0]
    return df0.drop(df0.index[0])
