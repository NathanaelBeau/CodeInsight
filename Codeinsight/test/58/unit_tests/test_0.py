arr0 = np.array([1, 5, 10, 15, 20])
var0 = 10
expected_result =  np.array([1, 5, 10, 0, 0])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'