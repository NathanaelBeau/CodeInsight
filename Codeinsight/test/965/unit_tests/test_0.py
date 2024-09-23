arr0 = np.array([[2, 4, 6], [3, 6, 9], [4, 8, 12]])
vec0 = np.array([2, 3, 4])
expected_result =  np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
result = test(arr0, vec0)
assert np.array_equal(result, expected_result), 'Test failed'