var0 = np.array([1, 2, 3])
var1 = np.array([4, 5, 6])
expected_result =  np.sqrt(27)
result = test(var0, var1)
assert result == expected_result, 'Test failed'