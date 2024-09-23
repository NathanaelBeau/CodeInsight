import pandas as pd
df0 = pd.DataFrame({('col1', 'a'): [1, 2], ('col1', 'b'): [3, 4], 'C': [5, 6]})
expected_result =  pd.DataFrame({('col1', 'b'): [3, 4], 'C': [5, 6]})
assert test(df0).equals(expected_result), 'Test failed'