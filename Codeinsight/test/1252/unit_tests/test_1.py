df0 = pd.DataFrame({'apple': [1, 2, 3], 'banana': [4, 5, 6], 'cherry': [7, 8, 9]})
str0 = 'a$'
expected_result =  pd.DataFrame({'banana': [4, 5, 6]})
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'