import pandas as pd
def test(df0, lst0, var0):
    return df0[lst0].apply(lambda x: var0 in x)

