lst0 = ['k3', 'k2', 'k1', 'k4']
var0 = 'k3'
expected_output = {'k3': [1], 'k2': [], 'k1': [], 'k4': []}
output = test(lst0, var0)
assert output == expected_output, 'Test failed'