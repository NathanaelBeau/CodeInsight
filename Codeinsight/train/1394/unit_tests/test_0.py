import pandas as pd
df0 = pd.DataFrame({'A': [0, 0, 0], 'B': [1, 0, 2], 'C': [0, 0, 0]})
expected_result =  pd.DataFrame({'B': [1, 0, 2]})
assert test(df0).equals(expected_result), 'Test failed'