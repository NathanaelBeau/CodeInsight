import pandas as pd

def test(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    combined_df = pd.concat([df1, df2])
    return combined_df.groupby(combined_df.index).mean()
