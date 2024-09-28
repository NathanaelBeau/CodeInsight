dict0 = {}
dict1 = {0: [1, 2, 3], 1: [4, 5], 2: [6, 7], 3: [8, 9]}
expected_output = {0: [], 1: [], 2: [], 3: []}
assert test(dict0, dict1) == expected_output, 'Test failed'