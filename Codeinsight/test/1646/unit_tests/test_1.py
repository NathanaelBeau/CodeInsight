arr0 = np.array([[7], [8], [9]])
var0 = 4
expected_result =  np.array([[[7, 7, 7, 7]], [[8, 8, 8, 8]], [[9, 9, 9, 9]]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'