import pandas as pd
df0 = pd.DataFrame({'id': [1, 2, 3], 'value': ['a', 'b', 'c']})
expected_result =  {1: 'a', 2: 'b', 3: 'c'}
assert test(df0) == expected_result, 'Test failed'