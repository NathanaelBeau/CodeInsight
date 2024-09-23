import pandas as pd

def test(series0, var0):
    indices = series0[series0 == var0].index
    return indices[0] if len(indices) > 0 else None

