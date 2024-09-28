arr1 = np.array([10, 20, -np.inf, 40, 50])
expected_result =  np.array([10, 20, 0, 40, 50])
result = test(arr1)
assert np.array_equal(result, expected_result), 'Test failed'