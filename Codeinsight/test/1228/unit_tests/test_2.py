# Test 3
ser0 = pd.Series([False, False, False])
expected_result =  pd.Series([True, True, True])
result = test(ser0)
assert result.equals(expected_result), 'Test failed'