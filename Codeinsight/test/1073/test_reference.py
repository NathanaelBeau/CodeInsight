import pandas as pd

def test(df0):
    result = []
    for index, row in df0.iterrows():
        result.append((index, row['A']))
    return result

