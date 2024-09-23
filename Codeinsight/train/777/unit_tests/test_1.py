dict0 = {'x': (8, 6), 'y': (4, 7), 'z': (3, 5)}
expected_result =  {'x': (8, 6), 'z': (3, 5), 'y': (4, 7)}
result = test(dict0)
assert result == expected_result, 'Test failed'