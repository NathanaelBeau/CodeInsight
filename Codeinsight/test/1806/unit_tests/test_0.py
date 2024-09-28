dict0 = {'somekey': 1, 'someotherkey': 2, 'somekeyggg': 3}
lst0 = ['somekey', 'someotherkey', 'somekeyggg']
expected_output = True
assert test(dict0, lst0) == expected_output, 'Test failed'