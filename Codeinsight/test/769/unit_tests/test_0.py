# Test 1
lst0 = [np.array([1, 2]), np.array([3, 4]), np.array([5, 6])]
expected_result =  np.array([1, 2, 3, 4, 5, 6])
result = test(lst0)
assert np.array_equal(result, expected_result), 'Test failed'