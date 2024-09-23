lst0 = [[1, 1], [1, 2], [2, 1], [1, 1], [3, 4]]
expected_result =  [[1, 2], [2, 1], [3, 4]]
result = test(lst0)
assert result == expected_result, 'Test failed'