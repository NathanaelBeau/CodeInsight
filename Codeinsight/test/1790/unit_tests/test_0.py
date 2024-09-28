dict0 = {'a': 10, 'b': 20, 'c': 30}
dict1 = {'a': 2, 'b': 5, 'd': 40}
expected_result =  {'a': 5.0, 'b': 4.0}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'