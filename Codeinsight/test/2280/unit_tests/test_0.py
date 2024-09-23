lst0 = [('apple',), ('banana',), ('orange',)]
var0 = ', '
expected_result =  'apple, banana, orange'
result = test(lst0, var0)
assert result == expected_result, 'Test failed'