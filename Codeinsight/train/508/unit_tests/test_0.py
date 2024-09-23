import pandas as pd
df0 = pd.DataFrame({ 'A': [1, 1, 2, 2, 3, 3], 'B': ['a', 'a', 'b', 'b', 'c', 'c'], 'C': [10, 20, 30, 40, 50, 60] })
expected_output = pd.DataFrame({ 'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [20, 40, 60] })
# Check if the output matches the expected output
assert test(df0).values.tolist() == expected_output.values.tolist(), 'Test failed'