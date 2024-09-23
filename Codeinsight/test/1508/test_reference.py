import pandas as pd

def test(df0, columns_list0):
    df0[columns_list0] = df0[columns_list0].applymap(lambda x: "{:.2%}".format(x))
    return df0

