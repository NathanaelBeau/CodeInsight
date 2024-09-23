import pandas as pd

def test(df0, lst0):
    df0['sum'] = df0[lst0[0]] + df0[lst0[1]]
    return df0