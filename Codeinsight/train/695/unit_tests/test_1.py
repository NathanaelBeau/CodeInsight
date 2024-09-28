# Test 2
lst0 = [np.array([7]), np.array([8, 9]), np.array([])]
expected_result =  np.array([7, 8, 9])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'