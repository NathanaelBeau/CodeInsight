import pandas as pd
df0 = pd.DataFrame({'A': [13, 14], 'B': [15, 16]}, index=['first', 'second'])
expected_result =  ['first', 'second']
assert test(df0) == expected_result, 'Test failed'