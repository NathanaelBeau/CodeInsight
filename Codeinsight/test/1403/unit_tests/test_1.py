arr0 = np.array([[5], [15], [25]])
vec0 = np.array([5, 15, 25])
expected_result =  np.array([[1], [1], [1]])
result = test(arr0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'