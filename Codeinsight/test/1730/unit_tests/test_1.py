var0 = r'x(y)z(\d)'
str0 = 'xyz1 and again xyz2'
expected_output = [('y', '1'), ('y', '2')]
assert test(var0, str0) == expected_output, 'Test failed'