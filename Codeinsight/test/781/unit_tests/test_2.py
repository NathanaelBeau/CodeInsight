import pandas as pd
df0 = pd.DataFrame({'A': [10, 20], 'B': [30, 40], 'column_name': [50, 60]})
expected_result =  pd.DataFrame({'A': [10, 20], 'B': [30, 40]})
assert test(df0, 'column_name').equals(expected_result), 'Test failed'