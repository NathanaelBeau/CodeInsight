df0 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
str0 = '^A'
expected_result =  pd.DataFrame({'A': [1, 2, 3]})
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'