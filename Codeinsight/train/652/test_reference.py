import pandas as pd

def test(df0, var0):
    positive_values = df0[df0[var0] > 0]
    return len(positive_values) / len(df0)
