series0 = pd.Series([4, 5, 6], name='B')
expected_result =  pd.DataFrame({'B': [4, 5, 6]})
result = test(series0)
assert result.equals(expected_result), 'Test failed'