import pandas as pd
df0 = pd.DataFrame({'A': [1, 2], 'B': [3, 4], 'C': [5, 6], 'D': [7, 8], 'E': [9, 10]})
expected_result =  pd.DataFrame({'C': [5, 6], 'E': [9, 10]})
assert test(df0).equals(expected_result), 'Test failed'