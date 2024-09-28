dict2 = {'one': 1, 'three': 3, 'five': 5, 'seven': 7}
lst2 = ['one', 'seven', 'nine']
expected_output3 = {'one': 1, 'seven': 7}
assert test(dict2, lst2) == expected_output3, 'Test failed'