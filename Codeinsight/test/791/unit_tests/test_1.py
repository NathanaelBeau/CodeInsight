# Test 2
mat0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
part = 'lower'
expected_result =  np.array([[1, 0, 0], [4, 5, 0], [7, 8, 9]])
result = test(mat0, part)
assert np.array_equal(result, expected_result), 'Test failed'