lst0 = [[0.0, 1.0, 2.0], [-1.0, -2.0, -3.0]]
var0= '{0:.8e}'
expected_output = [['0.00000000e+00', '1.00000000e+00', '2.00000000e+00'], ['-1.00000000e+00', '-2.00000000e+00', '-3.00000000e+00']]
assert test(lst0, var0) == expected_output, 'Test failed'