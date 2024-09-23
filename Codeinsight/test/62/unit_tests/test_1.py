dict0 = {'x': 15, 'y': 30}
dict1 = {'x': 3, 'y': 6}
expected_result =  {'x': 5.0, 'y': 5.0}
result = test(dict0, dict1)
assert result == expected_result, 'Test failed'