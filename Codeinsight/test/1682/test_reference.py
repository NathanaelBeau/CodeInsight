import pandas as pd
def test(df0, col_values, col_weights):
    return df0.apply(lambda row: row[col_values] * row[col_weights], axis=1).sum() / df0[col_weights].sum()

