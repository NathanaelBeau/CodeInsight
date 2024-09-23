import pandas as pd
df0 = pd.DataFrame({'A': [1, 2], 'column_name': [3, 4], 'C': [5, 6]})
expected_result =  pd.DataFrame({'A': [1, 2], 'C': [5, 6]})
assert test(df0, 'column_name').equals(expected_result), 'Test failed'