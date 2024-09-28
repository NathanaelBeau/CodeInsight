arr2 = np.array([0.1, 0.2, -np.inf, 0.3])
expected_result =  np.array([0.1, 0.2, 0, 0.3])
result = test(arr2)
assert np.array_equal(result, expected_result), 'Test failed'