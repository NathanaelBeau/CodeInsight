lst0 = [True, False, True, False]
var0 = ['a', 'b', 'c', 'd']
var1 = [1, 2, 3, 4]
expected_output = ['a', 2, 'c', 4]
output = test(lst0, var0, var1)
assert output == expected_output, 'Test failed'