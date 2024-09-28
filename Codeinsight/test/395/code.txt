import pandas as pd

def test(df0, column_name0, threshold0, column_name1):
    count_condition = (df0[column_name0] > threshold0).sum()
    sum_condition = df0.loc[df0[column_name0] > threshold0, column_name1].sum()
    return count_condition, sum_condition
