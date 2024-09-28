import pandas as pd
df0 = pd.DataFrame({'F': [1, 2], 'G': [3, 4], 'H': [5, 6], 'I': [7, 8], 'J': [9, 10]})
expected_result =  pd.DataFrame({'H': [5, 6], 'J': [9, 10]})
assert test(df0).equals(expected_result), 'Test failed'