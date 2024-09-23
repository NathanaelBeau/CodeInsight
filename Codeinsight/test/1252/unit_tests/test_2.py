df0 = pd.DataFrame({'cat': [1, 2, 3], 'dog': [4, 5, 6], 'bird': [7, 8, 9]})
str0 = '^[cd]'
expected_result =  pd.DataFrame({'cat': [1, 2, 3], 'dog': [4, 5, 6]})
result = test(df0, str0)
assert result.equals(expected_result), 'Test failed'