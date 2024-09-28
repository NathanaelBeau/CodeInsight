arr0 = np.array([-5, -4, -3, -2, -1])
var0 = -3
var1 = 0
expected_result =  np.array([-5, -4, -3, 0, 0])
result = test(arr0.copy(), var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'