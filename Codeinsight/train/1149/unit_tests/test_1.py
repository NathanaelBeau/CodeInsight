# Test 2
ser0 = pd.Series([True, True, True])
expected_result =  pd.Series([False, False, False])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'