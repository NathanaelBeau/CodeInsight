arr0 = np.array([100, 2, 56, 8, 25])
var0 = 2
expected_result =  np.array([1, 3])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'