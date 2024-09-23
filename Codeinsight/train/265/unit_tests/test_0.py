df0 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
str0 = 'A'
str1 = 2
expected_output = df0 = pd.DataFrame({'A': [2], 'B': ['b']})
assert test(df0, str0, str1).equals(expected_output), 'Test failed'