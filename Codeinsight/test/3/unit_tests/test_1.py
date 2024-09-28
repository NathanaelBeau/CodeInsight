dict0 = {'X': [10, 20], 'Y': [30, 40], 'Z': [50, 60]}
expected_output = {'Z': 110, 'Y': 70, 'X': 30}
assert test(dict0) == expected_output, 'Test failed'