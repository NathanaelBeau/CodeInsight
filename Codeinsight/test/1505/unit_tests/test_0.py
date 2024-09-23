arr0 = np.array([1.2345, 2.3456, 3.4567])
var0 = 2
expected_result =  np.array([1.23, 2.35, 3.46])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'