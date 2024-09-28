arr0 = np.array([10, 20, 30, 40, 50])
var0 = 3
expected_result =  np.array([0, 1, 2])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'