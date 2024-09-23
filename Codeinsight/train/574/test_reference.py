import pandas as pd

def test(df0, var0, var1):
    
    col_not_in_var0 = [x for x in list(df0.columns) if x not in var0]
    for i in range(len(var0)):
        col_not_in_var0.insert(var1[i], var0[i])

    return df0[col_not_in_var0].values.tolist()
