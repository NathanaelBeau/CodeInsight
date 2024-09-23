import pandas as pd
def test(df0):
    return pd.concat([df0.head(1), df0.tail(1)])
