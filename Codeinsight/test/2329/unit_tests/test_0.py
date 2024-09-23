arr0 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
var0 = 4
expected_result =  np.array([1, 2, 3, 5, 6, 7, 8])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'