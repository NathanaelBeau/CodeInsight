import pandas as pd
def test(df0, lst0):
    mapping = {name: i for i, name in enumerate(lst0)}
    df0['order'] = df0['name'].map(mapping)
    df0 = df0.sort_values('order').drop(columns='order').reset_index(drop=True)
    return df0