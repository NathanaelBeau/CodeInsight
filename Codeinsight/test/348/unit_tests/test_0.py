import pandas as pd
# Test 1
df0 = pd.DataFrame({ 'A': [1, 4], 'B': [2, 5], 'C': [3, 6], 'D': [7, 10], 'E': [8, 11], 'F': [9, 12] })
expected_output = pd.DataFrame({ 0: [2.0, 5.0], 1: [8.0, 11.0] })
assert test(df0).equals(expected_output), 'Test failed'