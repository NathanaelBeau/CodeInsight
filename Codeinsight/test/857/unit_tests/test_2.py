lst0 = np.array([0, 5, 10])
lst1 = np.array([0, 3, 6])
var0 = 6
var1 = 4
expected_result =  1
result = test(lst0, lst1, var0, var1)
assert result == expected_result, 'Test failed'