import pandas as pd

def test(df):
    return [{col: df[col].tolist()} for col in df.columns]

