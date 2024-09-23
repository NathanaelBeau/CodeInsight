dict0 = {'x': 12, 'y': 24}
dict1 = {'x': 3, 'y': 6}
expected_result =  {'x': 4.0, 'y': 4.0}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'