lst0 = [('red',), ('green',), ('blue',)]
var0 = '-'
expected_result =  'red-green-blue'
result = test(lst0, var0)
assert result == expected_result, 'Test failed'