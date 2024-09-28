dict0 = {'a': 1, 'b': 2}
dict1 = {'c': 3}
expected_result =  {'a': 1, 'b': 2, 'c': 3}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'