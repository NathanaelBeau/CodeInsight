import pandas as pd

def test(df0, column_name0, threshold0, column_name1):
    filtered_df = df0.query(f"{column_name0} > {threshold0}")
    count_condition = len(filtered_df)
    sum_condition = filtered_df[column_name1].sum()
    return count_condition, sum_condition

