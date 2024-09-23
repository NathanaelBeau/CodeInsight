import pandas as pd
def test(df0, var0):
    return df0.query("var0 == 1")['b'].sum()

