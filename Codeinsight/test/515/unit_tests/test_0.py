import pandas as pd
df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['x', 'y', 'z'])
expected_result =  ['x', 'y', 'z']
assert test(df0) == expected_result, 'Test failed'