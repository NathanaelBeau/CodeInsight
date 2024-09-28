arr0 = np.array([5, 7, 9, 12, 14])
var0 = 8
expected_result =  np.array([5, 7, 8, 8, 8])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'