import pandas as pd
def test(df0, var0, var1):
    return df0[var0].apply(lambda cell: var1 in cell).to_list()