dict0 = {'a': 'x', 'b': 'y'}
dict1 = {'x': 10, 'y': 20}
expected_result =  {'a': 10, 'b': 20}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'