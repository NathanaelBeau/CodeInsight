import pandas as pd
df0 = pd.DataFrame({'K': [1, 2], 'L': [3, 4], 'M': [5, 6], 'N': [7, 8], 'O': [9, 10]})
expected_result =  pd.DataFrame({'M': [5, 6], 'O': [9, 10]})
assert test(df0).equals(expected_result), 'Test failed'