# Test 1
ser0 = pd.Series([1, 2, 3, 4])
expected_result =  np.array([1, 2, 3, 4])
result = test(ser0)
assert np.array_equal(result, expected_result), 'Test failed'