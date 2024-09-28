import pandas as pd

def test(var0):
    df0 = var0.value_counts().rename_axis('value').reset_index(name='count')
    return df0
