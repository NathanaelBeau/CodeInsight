import pandas as pd
def test(df0, str0, lst0):
    return pd.cut(df0[str0], lst0)

