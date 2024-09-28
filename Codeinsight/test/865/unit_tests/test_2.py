arr0 = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
var0 = 0.2
var1 = 0.5
expected_result =  4
result = test(arr0, var0, var1)
assert result == expected_result, 'Test failed'