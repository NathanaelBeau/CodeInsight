import pandas as pd
def test(df0):
    result = pd.isna(df0[('col1', 'col2')]).any()
    return result
