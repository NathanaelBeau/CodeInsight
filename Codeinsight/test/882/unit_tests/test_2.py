# Test 3
arr0 = np.array([[11, 12], [13, 14], [15, 16], [17, 18]])
expected_result =  np.array([[11, 12], [13, 14], [15, 16], [17, 18]])
result = test(arr0)
assert np.array_equal(result, expected_result), 'Test failed'