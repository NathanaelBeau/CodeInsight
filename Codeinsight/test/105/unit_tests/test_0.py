vec0 = np.array([1, 2, 3])
num_times0 = 3
expected_result =  np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
result = test(vec0, num_times0)
assert np.array_equal(result, expected_result), 'Test failed'