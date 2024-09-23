import pandas as pd

def test(df0, var0):
    split_data = df0[var0].str[1:-1].str.split(',', expand=True)
    split_data = split_data.astype(float)
    split_data.columns = [f'col{i}' for i in range(1, len(split_data.columns)+1)]   
    return split_data

