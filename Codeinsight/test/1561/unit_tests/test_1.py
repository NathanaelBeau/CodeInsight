arr0 = np.array([5, 10, 15, 20, 25])
expected_min, expected_max = 5, 25
result_min, result_max = test(arr0)
assert result_min == expected_min and result_max == expected_max, 'Test failed'