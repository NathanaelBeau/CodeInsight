# Test 3
ser0 = pd.Series([True, False, True])
expected_result =  np.array([True, False, True])
result = test(ser0)
assert np.array_equal(result, expected_result), 'Test failed'