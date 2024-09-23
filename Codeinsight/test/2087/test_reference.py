import pandas as pd

def test(df: pd.DataFrame) -> list:
    return [row.to_dict() for _, row in df.iterrows()]

