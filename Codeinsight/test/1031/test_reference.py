import pandas as pd

def test(df0):
    nonzero_indices = df0[df0 != 0].stack().index.tolist()
    rows, cols = zip(*nonzero_indices)
    col_indices = [df0.columns.get_loc(col) for col in cols]
    mean_row = sum(rows) / len(rows)
    mean_col = sum(col_indices) / len(col_indices)
    return mean_row, mean_col

