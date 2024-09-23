import pandas as pd

def test(var0, var1, lst0, lst1):
    df = pd.DataFrame({var0: lst0, var1: lst1})
    tuples = list(zip(df[var0], df[var1]))
    return pd.factorize(tuples)[0]