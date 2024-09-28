import pandas as pd

def test(df0: pd.DataFrame) -> pd.DataFrame:
    return df0.apply(lambda row: sorted(row, reverse=True), axis=1, result_type='broadcast')