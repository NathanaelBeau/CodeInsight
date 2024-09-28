var0 = {'B': 2, 'A': 1, 'C': 3}
expected_result =  OrderedDict([('A', 1), ('B', 2), ('C', 3)])
result = test(var0)
assert result == expected_result, 'Test failed'