var0 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
var1 = 0
expected_result =  np.array([[[5, 6], [7, 8]], [[9, 10], [11, 12]]])
result = test(var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'