import pandas as pd

def test(df0, column_name0):
    percentile_25 = df0[column_name0].quantile(0.25)
    percentile_50 = df0[column_name0].quantile(0.50)
    percentile_75 = df0[column_name0].quantile(0.75)
    return percentile_25, percentile_50, percentile_75

