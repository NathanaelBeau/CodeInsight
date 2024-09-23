import pandas as pd

def test(df0, lst0, var0, var1):
    unpivoted = df0.melt(id_vars=lst0, var_name=var0, value_name=var1)
    return unpivoted
