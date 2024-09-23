import pandas as pd

def test(df: pd.DataFrame) -> list:
    return [{'index': idx, **row.to_dict()} for idx, row in df.iterrows()]

