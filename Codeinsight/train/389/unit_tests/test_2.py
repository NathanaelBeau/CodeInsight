import pandas as pd
df0 = pd.DataFrame({ 'A': [0, 1, 2, 3], 'B': [2, 0, -1, -2] })
expected_result3 = pd.DataFrame({ 'A': [2, 3], 'B': [-1, -2] }, index=[2, 3])
assert test(df0).equals(expected_result3), 'Test failed'