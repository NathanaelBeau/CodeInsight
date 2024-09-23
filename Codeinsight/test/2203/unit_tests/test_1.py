dict0 = {'a': 1, 'b': 3}
dict1 = {'a': 1, 'b': 2, 'c': 3}
expected_result =  False
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'