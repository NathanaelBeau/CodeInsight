dict0 = {'a': 1, 'b': 2, 'c': 3}
expected_result =  {'a', 'b', 'c'}
result = test(dict0)
assert result == expected_result, 'Test failed'