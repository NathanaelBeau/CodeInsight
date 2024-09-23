dict0 = { 'red': [5, 1, 8], 'green': [2, 3, 6], 'blue': [9, 4, 7] }
lst0 = 0
expected_output = [('green', [2, 3, 6]), ('red', [5, 1, 8]), ('blue', [9, 4, 7])]
assert test(dict0, lst0) ==expected_output, 'Test failed'