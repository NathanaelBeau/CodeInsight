arr0 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
var0 = 0
expected_result =  np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'