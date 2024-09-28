# Test 3
s0 = pd.Series([10, 20, 20, 30, 30, 30])
expected_result =  pd.DataFrame({'value': [30, 20, 10], 'count': [3, 2, 1]})
result = test(s0)
assert result.equals(expected_result), 'Test failed'