arg = [('1', '2'), ('3', '4'), ('5', '1')]
expected_output = [('1', '2'), ('5', '1')]
assert test(arg) == expected_output, 'Test failed'