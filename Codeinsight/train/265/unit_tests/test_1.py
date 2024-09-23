df0 = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c']})
str0 = 'B'
str1 = 'a'
expected_output =  df0 = pd.DataFrame({'A': [1], 'B': ['a']})
assert test(df0, str0, str1).equals(expected_output), 'Test failed'