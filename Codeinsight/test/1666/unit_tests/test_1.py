lst0 = [['A', 1], ['B', 2], ['C', 3], ['D', 4], ['E', 5]]
expected_result =  {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}
result = test(lst0)
assert result == expected_result, 'Test failed'