lst0 = [{'x': 10}, {'y': 20}, {'z': 30}]
expected_result =  {'x': 10, 'y': 20, 'z': 30}
result = test(lst0)
assert result == expected_result, 'Test failed'