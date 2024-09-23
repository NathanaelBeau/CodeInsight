import pandas as pd
def test(df0, col_values, col_weights):
    return (df0[col_values] * df0[col_weights]).sum() / df0[col_weights].sum()

