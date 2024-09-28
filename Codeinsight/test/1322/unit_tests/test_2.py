dict0 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
expected_output = (['one', 'two', 'three', 'four'], [1, 2, 3, 4])
assert test(dict0) == expected_output, 'Test failed'