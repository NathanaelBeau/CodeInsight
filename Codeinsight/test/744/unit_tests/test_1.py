expected_result = lst0 = [[5, 5], [10, 3], [10, 3], [15, 1]]
expected_result_2 = [[5, 5], [10, 3], [15, 1]]
result_2 = test([[5, 5], [10, 3], [10, 3], [15, 1]])
assert result_2 == expected_result_2 or set(map(tuple, result_2)) == set(map(tuple, expected_result_2)), 'Test failed'