import pandas as pd

def test(df0, df1, df2, col_name):
    dfs = [df.set_index(col_name) for df in [df0, df1, df2]]
    result = pd.concat(dfs, axis=1).reset_index()
    return result