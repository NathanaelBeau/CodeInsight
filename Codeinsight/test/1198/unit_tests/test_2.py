arr0 = np.array([[20, 21], [22, 23], [24, 25]])
var0 = 0
expected_result =  np.array([20, 22, 24])
result = test(arr0, var0)
assert np.array_equal(result, expected_result), 'Test failed'