import pandas as pd

def test(lst0, lst1):
    df_grouped = lst0.groupby([lst1[0], lst1[1]]).size()
    return df_grouped

