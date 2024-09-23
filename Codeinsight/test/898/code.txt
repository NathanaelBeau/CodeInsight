import pandas as pd

def test(df0, columns_list0):
    df0[columns_list0] = df0[columns_list0].applymap(lambda x: f"{x * 100:.2f}%")
    return df0