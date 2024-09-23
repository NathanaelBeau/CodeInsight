series0 = pd.Series([1, 2, 3], name='A')
expected_result =  pd.DataFrame({'A': [1, 2, 3]})
result = test(series0)
assert result.equals(expected_result), 'Test failed'