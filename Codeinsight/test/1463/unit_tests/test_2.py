dict0 = {'p': True, 'q': False, 'r': True, 's': True}
expected_result =  {True: ['p', 'r', 's']}
assert test(dict0) == expected_result, 'Test failed'