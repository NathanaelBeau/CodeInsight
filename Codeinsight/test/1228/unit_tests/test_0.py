# Test 1
ser0 = pd.Series([True, False, True, False])
expected_result =  pd.Series([False, True, False, True])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'