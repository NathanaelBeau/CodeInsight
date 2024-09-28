dict0 = {'zebra': 10, 'lion': 7, 'elephant': 15, 'giraffe': 9}
expected_output = [('lion', 7), ('giraffe', 9), ('zebra', 10), ('elephant', 15)]
assert test(dict0) == expected_output, 'Test failed'