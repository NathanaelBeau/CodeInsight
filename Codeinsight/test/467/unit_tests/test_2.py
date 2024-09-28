import pandas as pd
df0 = pd.DataFrame({('col1', 'a'): [10, 20], ('col1', 'b'): [30, 40], 'E': [50, 60]})
expected_result =  pd.DataFrame({('col1', 'b'): [30, 40], 'E': [50, 60]})
assert test(df0).equals(expected_result), 'Test failed'