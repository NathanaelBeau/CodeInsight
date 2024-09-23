import pandas as pd
def test(df0, df1, col0, col1):
    return pd.merge(df0, df1, left_on=col0, right_on=col1)
