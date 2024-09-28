import pandas as pd
df0 = pd.DataFrame({ 'A': [0, 1, 2, 3], 'B': [-2, 0, 1, 2] })
expected_result1 = pd.DataFrame({ 'A': [0, 2, 3], 'B': [-2, 1, 2] }, index=[0, 2, 3])
assert test(df0).equals(expected_result1), 'Test failed'