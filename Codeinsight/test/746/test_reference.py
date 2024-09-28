import pandas as pd

def test(var0, var1, var2):
    df = pd.DataFrame(columns=var0)
    df.loc[var1] = var2
    return df
