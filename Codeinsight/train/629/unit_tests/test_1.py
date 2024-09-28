import pandas as pd
df0 = pd.DataFrame({'A': [1, 2, 3], 'Value': [True, False, True]})
expected_output = pd.DataFrame({'A': [1, 3], 'Value': [True, True]}, index=[0,2])
assert test(df0).equals(expected_output), 'Test failed'