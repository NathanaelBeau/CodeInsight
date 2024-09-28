lst0 = [[3, 1], [6, 2], [3, 1], [9, 3]]
expected_result_3 = [[3, 1], [6, 2], [9, 3]]
result_3 = test([[3, 1], [6, 2], [3, 1], [9, 3]])
assert result_3 == expected_result_3 or set(map(tuple, result_3)) == set(map(tuple, expected_result_3)), 'Test failed'