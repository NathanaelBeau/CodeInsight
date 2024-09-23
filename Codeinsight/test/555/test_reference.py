import pandas as pd

def test(df0):
    sorted_df = df0.apply(lambda row: sorted(row.values), axis=1)
    return pd.DataFrame(sorted_df.values.tolist(), columns=df0.columns)