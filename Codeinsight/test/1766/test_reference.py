import pandas as pd

def test(df0, lst0):
    df0['sum'] = df0[lst0].sum(axis=1)
    df0['sum'] = df0.apply(lambda row: row[lst0[0]] + row[lst0[1]], axis=1)
    return df0