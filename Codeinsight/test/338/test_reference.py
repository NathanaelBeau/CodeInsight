import pandas as pd

def test(df: pd.DataFrame) -> list:
    return df.reset_index().to_dict(orient='records')
