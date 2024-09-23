import pandas as pd
def test(df0, col_name, var0):
    return df0.groupby(col_name, group_keys=False).apply(lambda x: x.sample(min(len(x), var0)))

