df0 = pd.DataFrame({'col': ['A', 'B', 'C']})
col0 = 'col'
expected_output = pd.DataFrame({'col': [0, 1, 2]})
assert test(df0, col0) .equals(expected_output), 'Test failed'