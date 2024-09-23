
import pandas as pd

def test(df0, col_name1, col_name2):
    return df0.set_index(col_name1)[col_name2].to_dict()

