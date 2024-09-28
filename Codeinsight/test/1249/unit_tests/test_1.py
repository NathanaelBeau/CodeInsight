import pandas as pd
df0 = pd.DataFrame({'A': [0, 1, 2], 'B': [1, 2, 3], 'C': [0, 0, 0]})
expected_result =  pd.DataFrame({'A': [0, 1, 2], 'B': [1, 2, 3]})
assert test(df0).equals(expected_result), 'Test failed'