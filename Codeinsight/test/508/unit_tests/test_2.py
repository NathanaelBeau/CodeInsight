lst0 = [('apple', 1), ('banana', 2), ('pear', 3), ('apple', 4)]
var0 = 'apple'
result = test(lst0, var0)
expected_result =  [('apple', 1), ('apple', 4)]
assert result == expected_result, 'Test failed'