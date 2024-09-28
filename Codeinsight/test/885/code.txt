import pandas as pd
def test(var0, var1, lst0, lst1):
    df = pd.DataFrame({var0: lst0, var1: lst1})
    return pd.factorize(df[[var0, var1]].apply(tuple, axis=1))[0]