dict0 = {'a': 1, 'b': 0, 'c': None, 'd': 'hello', 'e': False}
expected_result =  {'a': 1, 'd': 'hello'}
assert test(dict0) == expected_result, 'Test failed'