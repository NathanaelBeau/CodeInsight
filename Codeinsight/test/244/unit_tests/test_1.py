dict0 = { 'dog': [9, 12, 15], 'cat': [2, 6, 8], 'bird': [3, 5, 11] }
lst0 = 2
expected_output = [('cat', [2, 6, 8]), ('bird', [3, 5, 11]), ('dog', [9, 12, 15])]
assert test(dict0, lst0) ==expected_output, 'Test failed'