mat0 = np.array([[1, 2], [3, 4]])
vec0 = np.array([0.5, 0.5])
expected_result =  np.array([1.5, 3.5])
result = test(mat0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'