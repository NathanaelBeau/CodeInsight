lst0 = [1, 2, 3, 4, 5]
var0 = 2
lst1 = ['a', 'b', 'c']
expected_result =  [1, 2, 'a', 'b', 'c', 3, 4, 5]
result = test(lst0, var0, lst1)
assert result == expected_result, 'Test failed'