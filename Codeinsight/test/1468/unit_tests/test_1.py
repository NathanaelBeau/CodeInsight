mat1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
var0, var1 = 0, 2
expected_result =  np.array([[[1, 5], [3, 7]], [[2, 6], [4, 8]]])
result = test(mat1, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'