mat2 = np.array([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
var0, var1 = 1, 2
expected_result =  np.array([[[9, 11], [10, 12]], [[13, 15], [14, 16]]])
result = test(mat2, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'