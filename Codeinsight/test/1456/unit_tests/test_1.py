arr0 = np.array([10.5555, 20.6666])
var0 = 1
expected_result =  np.array([10.6, 20.7])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'