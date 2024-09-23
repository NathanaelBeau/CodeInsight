import pandas as pd
df0 = pd.DataFrame({ 'A': ['foo', 'foo', 'foo', 'foo'], 'B': [5, 6, 7, 8] })
expected_result2 = df0
assert test(df0).equals(expected_result2), 'Test failed'