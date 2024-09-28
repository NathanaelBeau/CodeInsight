import pandas as pd

def test(df0, df1):
    result_df = pd.DataFrame()
    for column in df0.columns:
        result_df[column] = df0[column] * df1[column]
    return result_df
