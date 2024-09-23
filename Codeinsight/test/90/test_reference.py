import pandas as pd

def test(var0, var1, lst0, lst1):
    df = pd.DataFrame({var0: lst0, var1: lst1})
    cat = pd.Categorical(df.apply(tuple, axis=1))
    return cat.codes
