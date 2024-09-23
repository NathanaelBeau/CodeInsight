import pandas as pd
df0 = pd.DataFrame({ 'A': [0, -1, 2, -3], 'B': [-2, -3, 0, 2] })
expected_result2 = pd.DataFrame({ 'A': [0, -1, 2], 'B': [-2, -3, 0] }, index=[0, 1, 2])
assert test(df0).equals(expected_result2), 'Test failed'