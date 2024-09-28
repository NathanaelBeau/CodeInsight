# Test 3
lst0 = [np.array([10, 11, 12]), np.array([]), np.array([])]
expected_result =  np.array([10, 11, 12])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'