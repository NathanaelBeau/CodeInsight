lst0 = np.array([-1, 0, 1])
lst1 = np.array([1, 0, -1])
var0 = 0.1
var1 = 0.2
expected_result =  1
result = test(lst0, lst1, var0, var1)
assert result == expected_result, 'Test failed'