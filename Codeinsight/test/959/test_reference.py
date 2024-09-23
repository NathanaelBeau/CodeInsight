import pandas as pd

def test(series0, var0):
    try:
        return series0.tolist().index(var0)
    except ValueError:
        return None

