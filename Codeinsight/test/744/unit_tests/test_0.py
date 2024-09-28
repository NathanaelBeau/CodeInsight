lst0 = [[1, 2], [1, 2], [3, 4], [5, 6]]
expected_result_1 = [[1, 2], [3, 4], [5, 6]]
result_1 = test([[1, 2], [1, 2], [3, 4], [5, 6]])
assert result_1 == expected_result_1 or set(map(tuple, result_1)) == set(map(tuple, expected_result_1)), 'Test failed'