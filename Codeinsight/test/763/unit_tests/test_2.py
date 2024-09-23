dict0 = {'one': 100, 'two': 50, 'three': 75, 'four': 25}
expected_output = [('four', 25), ('two', 50), ('three', 75), ('one', 100)]
assert test(dict0) == expected_output, 'Test failed'