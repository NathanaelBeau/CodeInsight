import pandas as pd

def test(df0, lst0, var0):
    filtered_rows = [row for _, row in df0.iterrows() if row[var0] in lst0]
    return pd.DataFrame(filtered_rows, columns=df0.columns)
