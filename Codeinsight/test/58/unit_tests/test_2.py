arr0 = np.array([-5, -4, -3, -2, -1, 0])
var0 = -3
expected_result =  np.array([-5, -4, -3, 0, 0, 0])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'