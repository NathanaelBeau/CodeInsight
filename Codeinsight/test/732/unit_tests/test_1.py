dict0 = {'HeLLo': 'WoRLD', 'pyTHOn': 'RoCks'}
expected_result =  {'hello': 'world', 'python': 'rocks'}
result = test(dict0)
assert result == expected_result, 'Test failed'