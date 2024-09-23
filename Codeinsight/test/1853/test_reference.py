import pandas as pd

def test(df0, var0, agg_function):
    grouped = df0.groupby(var0).agg(agg_function)
    return grouped.reset_index()

