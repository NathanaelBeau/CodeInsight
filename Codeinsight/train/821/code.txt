import pandas as pd

def test(df0, df1, var0):
    merged_df = df0.merge(df1, on=var0, suffixes=('', '_y'))
    return merged_df.filter(regex='^(?!.*_y)')
