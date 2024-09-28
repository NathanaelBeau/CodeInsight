mat0 = np.array([[0, 1], [1, 0]])
vec0 = np.array([2, 3])
expected_result =  np.array([3, 2])
result = test(mat0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'