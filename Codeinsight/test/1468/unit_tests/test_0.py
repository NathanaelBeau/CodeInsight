mat0 = np.array([[1, 2, 3], [4, 5, 6]])
var0, var1 = 0, 1
expected_result =  np.array([[1, 4], [2, 5], [3, 6]])
result = test(mat0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'