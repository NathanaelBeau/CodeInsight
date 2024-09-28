dict0 = {'b': 20, 'a': 30, 'c': 10}
expected_result =  {'c': 10, 'b': 20, 'a': 30}
result = test(dict0)
assert result == expected_result, 'Test failed'