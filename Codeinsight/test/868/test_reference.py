import numpy as np
def test(df0, lst0):
    return df0[lst0].apply(pd.Series.value_counts)
