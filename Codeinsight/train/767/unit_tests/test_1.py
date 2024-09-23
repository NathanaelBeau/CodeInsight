dict0 = {'HELLO': 'world', 'PYTHON': 'rules'}
expected_result =  {'hello': 'world', 'python': 'rules'}
result = test(dict0)
assert result == expected_result, 'Test failed'