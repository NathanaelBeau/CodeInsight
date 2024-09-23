lst0 = ['x', 'y', 'z']
lst1 = [10, 20, 30]
expected_result =  {'x': 10, 'y': 20, 'z': 30}
result = test(lst0, lst1)
assert result == expected_result, 'Test failed'