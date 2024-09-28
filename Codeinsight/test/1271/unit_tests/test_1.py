import pandas as pd
df0 = pd.DataFrame({'A': ['-', '-', '-'], 'B': ['-', 5, 6]})
expected_result =  pd.DataFrame({'A': [np.nan, np.nan, np.nan], 'B': [np.nan, 5, 6]})
assert test(df0).equals(expected_result), 'Test failed'