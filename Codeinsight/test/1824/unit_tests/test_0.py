df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
str0 = 'B'
expected_output = pd.DataFrame({'A': [1, 2, 3], 'C': [7, 8, 9]})
assert test(df0, str0) .equals( expected_output), 'Test failed'