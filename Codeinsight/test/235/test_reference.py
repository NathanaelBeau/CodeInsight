import pandas as pd

def test(df0, lst0, var0, var1):
    cols_to_melt = [col for col in df0.columns if col not in lst0]
    unpivoted = pd.melt(df0, id_vars=lst0, value_vars=cols_to_melt, var_name=var0, value_name=var1)
    return unpivoted

