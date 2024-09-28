import pandas as pd
def test(df0, var0):
    return {key: df0.drop(columns=[var0]).iloc[i].tolist() for i, key in enumerate(df0[var0])}

