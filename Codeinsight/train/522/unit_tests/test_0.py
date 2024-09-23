dict0 = {'A': 'Apple', 'B': 'Banana', 'C': 'Cherry'}
dict1 = {'A': 1, 'B': 2, 'C': 3}
expected_output = {'Apple': 1, 'Banana': 2, 'Cherry': 3}
assert test(dict0, dict1) ==expected_output, 'Test failed'