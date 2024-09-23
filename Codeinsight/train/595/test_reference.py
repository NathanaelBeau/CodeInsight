import pandas as pd
def test(df0, var0):
    result_dict = {}
    for index, row in df0.iterrows():
        key = row[var0]
        row_dict = row.to_dict()
        row_dict.pop(var0)
        result_dict[key] = list(row_dict.values())
    return result_dict

