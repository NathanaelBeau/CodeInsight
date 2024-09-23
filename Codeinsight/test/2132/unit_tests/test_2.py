import pandas as pd
df0 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
expected_result =  pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})  # No '-' to replace
assert test(df0).equals(expected_result), 'Test failed'