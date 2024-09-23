df0 = pd.DataFrame({'A': [1, 2, 3]})
expected_output = pd.DataFrame({'A': [1, 2, 3]})
assert test(df0) .equals(expected_output), 'Test failed'