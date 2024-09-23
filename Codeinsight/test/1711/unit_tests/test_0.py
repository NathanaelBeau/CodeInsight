df0 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
expected_result =  pd.Series([4, 5, 6], name='b')
result = test(df0)
assert result.equals(expected_result), 'Test failed'