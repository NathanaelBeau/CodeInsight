lst0 = [[1, 2, 3], [4, 5, 1], [6, 7, 2]]
expected_result =  [[4, 5, 1], [6, 7, 2], [1, 2, 3]]
result = test(lst0)
assert result == expected_result, 'Test failed'