arr0 = np.array([1, 3, 7, 1, 2, 6, 3, 4, 5, 1])
expected_min, expected_max = 1, 7
result_min, result_max = test(arr0)
assert result_min == expected_min and result_max == expected_max, 'Test failed'