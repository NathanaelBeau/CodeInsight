var0 = {'D': 4, 'F': 6, 'E': 5}
expected_result =  OrderedDict([('D', 4), ('E', 5), ('F', 6)])
result = test(var0)
assert result == expected_result, 'Test failed'