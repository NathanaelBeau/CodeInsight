df0 = pd.DataFrame({'col0': [1, 2, 3], 'data': ['A', 'B', 'C']})
df1 = pd.DataFrame({'col1': [1, 2, 3], 'info': ['X', 'Y', 'Z']})
col0 = 'col0'
col1 = 'col1'
expected_output = pd.DataFrame({'col0': [1, 2, 3], 'data': ['A', 'B', 'C'], 'col1': [1, 2, 3], 'info': ['X', 'Y', 'Z']})
assert test(df0, df1, col0, col1) .equals(expected_output), 'Test failed'