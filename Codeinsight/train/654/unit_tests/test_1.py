lst0 = [['+', '-', '/'], ['*', '*', '+'], ['-', '/', '+']]
dict0 = {'*': 3, '/': 1, '+': 2, '-': 0}
expected_output = [['-', '/', '+'], ['+', '*', '*'], ['-', '/', '+']]
assert test(lst0, dict0) ==expected_output, 'Test failed'