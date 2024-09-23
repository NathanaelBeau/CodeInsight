import pandas as pd

def test(lst0):
    return lst0[lst0.isin(lst0.value_counts()[lst0.value_counts() > 1].index)].unique().tolist()
