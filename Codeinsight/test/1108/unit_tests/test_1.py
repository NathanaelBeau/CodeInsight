dict0 = { 'x': [100, 'alpha'], 'y': [50, 'beta'], 'z': [200, 'gamma'] }
var0 = 1
expected_output = ['x', 'y', 'z']
assert test(dict0, var0) ==expected_output, 'Test failed'