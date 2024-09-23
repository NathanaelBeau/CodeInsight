import pandas as pd
def test(var0, df0):
    return df0.join(var0)[[var0.name] + df0.columns.tolist()]

