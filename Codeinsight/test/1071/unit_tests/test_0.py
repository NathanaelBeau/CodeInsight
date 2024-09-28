dict0 = {'a': 1, 'b': 2}
dict1 = {'a': 1, 'b': 2, 'c': 3}
expected_result =  True
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'