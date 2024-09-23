import pandas as pd
def test(df0, lst0, var0):
    original_dtype = df0[var0].dtype
    df0[var0] = pd.Categorical(df0[var0], categories=lst0, ordered=True)
    sorted_df = df0.sort_values(by=[var0])
    sorted_df[var0] = sorted_df[var0].astype(original_dtype)
    return sorted_df
