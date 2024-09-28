import pandas as pd

def test(df0, col0, var0, var1):
    return df0.replace({col0: {var0: var1}})


