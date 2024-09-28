arr0 = [1.79769313486e+308, float('+inf'), float('-inf')]
expected_output = [1.79769313486e+308, float('-inf')]
assert test(arr0) ==expected_output, 'Test failed'