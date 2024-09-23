arr0 = np.array([10, 20, 30, 40, 50])
var0 = 25
var1 = -1
expected_result =  np.array([10, 20, -1, -1, -1])
result = test(arr0, var0, var1)
assert np.array_equal(result, expected_result), 'Test failed'