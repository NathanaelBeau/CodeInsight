import pandas as pd

def test(df1, df2, var0):
    new_df = pd.DataFrame({
        'df1': df1[var0],
        'df2': df2[var0]
    })
    return new_df
