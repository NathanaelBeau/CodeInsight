import pandas as pd
def test(df0, col0, var0):
    return next(iter(df0[df0[col0] == var0].index), None)