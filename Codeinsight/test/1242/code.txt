import pandas as pd
def test(df0):
    return df0.apply(pd.Series.value_counts, axis=1).fillna(0)
