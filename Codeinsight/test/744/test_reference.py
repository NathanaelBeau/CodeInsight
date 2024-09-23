import pandas as pd

def test(var0, df0):
    return pd.DataFrame(df0.values, columns=pd.MultiIndex.from_tuples([(var0, col) for col in df0.columns]))

