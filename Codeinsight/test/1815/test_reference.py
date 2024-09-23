import pandas as pd

def test(df0, str0, var1, str1):
    expanded_series = df0[str0].str.split(var1).apply(pd.Series, 1).stack()
    expanded_series.index = expanded_series.index.droplevel(-1)
    expanded_series.name = str0
    del df[str0]
    result_df = df0.join(expanded_series).reset_index(drop=True)
    return result_df[str1]

