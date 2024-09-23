import pandas as pd
df0 = pd.DataFrame({('col1', 'a'): [1, 2, 3], ('col1', 'b'): [4, 5, 6], 'D': [7, 8, 9]})
expected_result =  pd.DataFrame({('col1', 'b'): [4, 5, 6], 'D': [7, 8, 9]})
assert test(df0).equals(expected_result), 'Test failed'