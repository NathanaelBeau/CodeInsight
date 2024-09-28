lst0 = [['/', '+', '*'], ['-', '*', '+'], ['+', '/', '-']]
dict0 = {'*': 2, '/': 1, '+': 3, '-': 0}
expected_output = [['/', '*', '+'], ['-', '*', '+'], ['-', '/', '+']]
assert test(lst0, dict0) ==expected_output, 'Test failed'