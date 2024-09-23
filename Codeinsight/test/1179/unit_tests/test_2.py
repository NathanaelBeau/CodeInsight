arr0 = np.array([-5, -4, -3, -2, -1])
expected_min, expected_max = -5, -1
result_min, result_max = test(arr0)
assert result_min == expected_min and result_max == expected_max, 'Test failed'