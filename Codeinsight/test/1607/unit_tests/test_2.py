series0 = pd.Series([7, 8, 9], name='C')
expected_result =  pd.DataFrame({'C': [7, 8, 9]})
result = test(series0)
assert result.equals(expected_result), 'Test failed'