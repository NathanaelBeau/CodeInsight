dict0 = {'HELLO': 'WORLD', 'PYTHON': 'ROCKS'}
expected_result =  {'hello': 'world', 'python': 'rocks'}
result = test(dict0)
assert result == expected_result, 'Test failed'