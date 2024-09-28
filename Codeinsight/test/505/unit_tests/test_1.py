var0 = {'Z': 26, 'Y': 25, 'X': 24}
expected_result =  OrderedDict([('X', 24), ('Y', 25), ('Z', 26)])
result = test(var0)
assert result == expected_result, 'Test failed'