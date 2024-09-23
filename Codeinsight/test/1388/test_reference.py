import pandas as pd
def test(df0, col1, col2):
    freq_list = []
    for index, row in df0.groupby([col1, col2]).size().reset_index().iterrows():
        freq_list.append((row[col1], row[col2], row[0]))
    return freq_list

