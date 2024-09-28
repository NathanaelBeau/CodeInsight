import pandas as pd
df0 = pd.DataFrame({'column_name': [1, 2, 3], 'D': [4, 5, 6]})
expected_result =  pd.DataFrame({'D': [4, 5, 6]})
assert test(df0, 'column_name').equals(expected_result), 'Test failed'