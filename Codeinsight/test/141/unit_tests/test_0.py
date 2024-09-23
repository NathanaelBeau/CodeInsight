matrix0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vec0 = np.array([1, 2, 3])
expected_result =  np.array([[0, 1, 2], [2, 3, 4], [4, 5, 6]])
result = test(matrix0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'