import pandas as pd
def test(df0, lst0):
    df0['name'] = pd.Categorical(df0['name'], categories=lst0, ordered=True)
    df0 = df0.sort_values('name').reset_index(drop=True)
    df0['name'] = df0['name'].astype(str)
    return df0
