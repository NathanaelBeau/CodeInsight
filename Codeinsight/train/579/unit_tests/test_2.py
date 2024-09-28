var0 = np.array([10, 20, 30])
var1 = np.array([10, 20, 30, 40, 50])
expected_result =  False
result = test(var0, var1)
assert result == expected_result, 'Test failed'