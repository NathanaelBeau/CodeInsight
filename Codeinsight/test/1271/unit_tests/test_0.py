import pandas as pd
df0 = pd.DataFrame({'A': [1, '-'], 'B': [3, 4]})
expected_result =  pd.DataFrame({'A': [1, np.nan], 'B': [3, 4]})
assert test(df0).equals(expected_result), 'Test failed'