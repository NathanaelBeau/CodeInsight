df0 = pd.DataFrame({'col': ['Apple', 'Banana', 'Orange', 'Apple']})
col0 = 'col'
expected_output = pd.DataFrame({'col': [0, 1, 2, 0]})
assert test(df0, col0) .equals(expected_output), 'Test failed'