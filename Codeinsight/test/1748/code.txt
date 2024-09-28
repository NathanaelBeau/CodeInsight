import pandas as pd

def test(df0, var0):
    def get_column_name(row):
        matching_columns = row[row == var0].index
        return matching_columns[0] if len(matching_columns) > 0 else None

    result = df0.apply(get_column_name, axis=1)
    result = result.astype(str) + " " + result.notnull().astype(str)
    return result