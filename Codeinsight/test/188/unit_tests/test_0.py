dict0 = {0: [11, 25], 1: [38], 2: [11, 18], 3: [11, 25]}
dict1 = {0: [11, 25, 38], 1: [38], 2: [11, 18], 3: [11, 25]}
expected_output = {0: [25, 11], 1: [38], 2: [18, 11], 3: [25, 11]}
assert test(dict0, dict1) == expected_output, 'Test failed'