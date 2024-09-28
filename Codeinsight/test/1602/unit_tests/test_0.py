lst0 = np.array([1, 2, 3])
lst1 = np.array([1, 2, 3])
var0 = 2.1
var1 = 2.1
expected_result =  1
result = test(lst0, lst1, var0, var1)
assert result == expected_result, 'Test failed'