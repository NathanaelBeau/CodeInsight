
import pandas as pd

def test(df0, col_name1, col_name2):
    return dict(zip(df0[col_name1], df0[col_name2]))
