# Test 1
mat0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
columns_to_delete = [2]
expected_result =  np.array([[1, 2], [4, 5], [7, 8]])
result = test(mat0, columns_to_delete)
assert np.array_equal(result, expected_result), 'Test failed'