import pandas as pd
df0 = pd.DataFrame({ 'A': ['foo', 'bar', 'foo', 'baz'], 'B': [1, 2, 3, 4] })
expected_result1 = pd.DataFrame({ 'A': ['foo', 'foo'], 'B': [1, 3] }, index=[0, 2])
assert test(df0).equals(expected_result1), 'Test failed'