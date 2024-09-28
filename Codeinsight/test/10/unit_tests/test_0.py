dict0 = {'a': 1, 'b': 2, 'c': 3}
dict1 = {'b': 4, 'c': 5, 'd': 6}
expected_result =  {'b': 2, 'c': 3}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'