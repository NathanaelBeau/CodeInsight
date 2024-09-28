# Test 2
mat0 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
columns_to_delete = [0, 3]
expected_result =  np.array([[2, 3], [6, 7], [10, 11]])
result = test(mat0, columns_to_delete)
assert np.array_equal(result, expected_result), 'Test failed'