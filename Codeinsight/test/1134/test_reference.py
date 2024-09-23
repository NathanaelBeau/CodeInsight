import pandas as pd

def test(df0, var0, lst0, op0):
    if op0 == 'in':
        return df0[df0[var0].isin(lst0)]
    elif op0 == 'not in':
        return df0[~df0[var0].isin(lst0)]
    else:
        raise ValueError("Invalid operation. Choose either 'in' or 'not in'.")

