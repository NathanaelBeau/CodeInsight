import pandas as pd
def test(df0, lst0, var0):
    custom_order = {v: i for i, v in enumerate(lst0)}
    return df0.sort_values(by=[var0], key=lambda col: col.map(custom_order))
