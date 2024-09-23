vec0 = np.array([4, 5])
num_times0 = 4
expected_result =  np.array([[4, 5], [4, 5], [4, 5], [4, 5]])
result = test(vec0, num_times0)
assert np.array_equal(result, expected_result), 'Test failed'