import pandas as pd
def test(df0, df1, var0):
    return pd.merge(df0, df1, on=var0, how='outer')
