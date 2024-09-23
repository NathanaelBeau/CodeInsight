dict0 = {0: [1, 2, 3], 1: [4, 5], 2: [6, 7], 3: [8, 9]}
dict1 = {0: [2, 3, 4], 1: [5, 6], 2: [7, 8], 3: [9, 10]}
expected_output = {0: [2, 3], 1: [5], 2: [7], 3: [9]}
assert test(dict0, dict1) == expected_output, 'Test failed'