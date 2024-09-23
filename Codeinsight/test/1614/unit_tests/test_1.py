arr0 = [float('+inf'), 1.0, 2.0, float('+inf'), 3.0]
expected_output = [1.0, 2.0, 3.0]
assert test(arr0) ==expected_output, 'Test failed'