dict0 = {'x': {'count': 1}, 'y': {'count': 2}, 'z': {'count': 2}}
expected_result =  'y'
result = test(dict0)
assert result == expected_result, 'Test failed'