var0 = {'alpha': True, 'beta': False, 'gamma': True}
expected_result =  [('beta', False), ('alpha', True), ('gamma', True)]
result = test(var0)
assert result == expected_result, 'Test failed'