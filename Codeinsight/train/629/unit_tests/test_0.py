import pandas as pd
df0 = pd.DataFrame({'A': [7, 8, 9], 'Value': [True, True, True]})
expected_output = pd.DataFrame({'A': [7, 8, 9], 'Value': [True, True, True]})
test3 = test(df0).equals(expected_output)
assert test3, 'Test failed'