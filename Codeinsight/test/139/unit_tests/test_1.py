lst0 = [10, 20, 30, 40, 50]
var0 = 0
lst1 = ['x', 'y']
expected_result =  ['x', 'y', 10, 20, 30, 40, 50]
result = test(lst0, var0, lst1)
assert result == expected_result, 'Test failed'