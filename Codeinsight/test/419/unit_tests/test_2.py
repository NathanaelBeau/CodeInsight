# Test 3
mat0 = np.array([[1, 2], [3, 4], [5, 6]])
columns_to_delete = [0, 1]
expected_result =  np.empty((3, 0))
result = test(mat0, columns_to_delete)
assert np.array_equal(result, expected_result), 'Test failed'