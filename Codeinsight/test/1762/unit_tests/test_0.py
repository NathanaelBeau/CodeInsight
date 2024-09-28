s0 = pd.Series([1, 2, 2, 3, 3, 3])
expected_result =  pd.DataFrame({'value': [3, 2, 1], 'count': [3, 2, 1]})
result = test(s0)
assert result.equals(expected_result), 'Test failed'