dict0 = {'first': 'alpha', 'second': 'beta'}
dict1 = {'alpha': 1, 'beta': 2}
expected_result =  {'first': 1, 'second': 2}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'