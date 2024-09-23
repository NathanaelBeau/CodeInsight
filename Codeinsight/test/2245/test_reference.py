import pandas as pd

def test(df0, column_name0, threshold0):
    return len(df0[df0[column_name0] > threshold0])

