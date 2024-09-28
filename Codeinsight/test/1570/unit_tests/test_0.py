dict0 = {'a': True, 'b': True, 'c': False, 'd': True}
expected_output = False
test(dict0) == expected_output
assert test(dict0) == expected_output, 'Test failed'