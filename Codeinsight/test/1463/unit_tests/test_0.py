dict0 = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
expected_result =  {2: ['b', 'c']}
assert test(dict0) == expected_result, 'Test failed'