dict0 = {'Hello1': 'WORLD2', 'Python3': 'Rocks4'}
expected_result =  {'hello1': 'world2', 'python3': 'rocks4'}
result = test(dict0)
assert result == expected_result, 'Test failed'