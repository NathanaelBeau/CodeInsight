df0 = pd.DataFrame({'a': [0.1, 0.2, 0.3], 'b': [0.4, 0.5, 0.6], 'c': [0.7, 0.8, 0.9]})
expected_result =  pd.Series([0.4, 0.5, 0.6], name='b')
result = test(df0)
assert result.equals(expected_result), 'Test failed'