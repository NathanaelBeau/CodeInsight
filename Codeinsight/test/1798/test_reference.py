import pandas as pd

def test(df0, lst0):
    return sorted(df0[lst0].stack().unique())

