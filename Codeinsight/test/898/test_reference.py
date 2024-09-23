import pandas as pd

def test(df0, columns_list0):
    format_dict = {col: "{:.2%}" for col in columns_list0}
    return df0.style.format(format_dict)

