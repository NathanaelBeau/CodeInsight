lst0 = [{'x': 10, 'y': 20}, {'z': 30}, {'x': 5, 'z': 15}]
expected_output = {'x', 'y', 'z'}
assert test(lst0) == expected_output, 'Test failed'