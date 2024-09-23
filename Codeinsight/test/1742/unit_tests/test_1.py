import pandas as pd
df0 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]}, index=['alpha', 'beta', 'gamma'])
expected_result =  ['alpha', 'beta', 'gamma']
assert test(df0) == expected_result, 'Test failed'