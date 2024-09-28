var0 = np.array([1, 2, 3, 4, 5])
var1 = np.array([1, 2, 3])
expected_result =  True
result = test(var0, var1)
assert expected_result == result, 'Test failed'