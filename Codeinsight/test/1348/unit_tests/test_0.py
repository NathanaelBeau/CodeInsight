lst0 = [[1, 2, 3], [4, 5, 6]]
expected_result =  [[0, 1, 0, 2, 0, 3], [0, 4, 0, 5, 0, 6]]
result = test(lst0)
assert result == expected_result, 'Test failed'