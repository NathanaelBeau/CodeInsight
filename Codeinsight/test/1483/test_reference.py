import pandas as pd

def test(df0, df1):
    result_df = pd.DataFrame(df0.values * df1.values, columns=df0.columns, index=df0.index)
    return result_df

