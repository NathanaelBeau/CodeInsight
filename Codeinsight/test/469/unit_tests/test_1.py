var0 = np.array([10, 20, 30, 40, 50])
var1 = np.array([10, 20, 30])
expected_result =  True
result = test(var0, var1)
assert result == expected_result, 'Test failed'